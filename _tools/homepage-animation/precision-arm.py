"""Authored forearm surfaces and joint hardware; original hand rig is retained."""
import math
import xml.etree.ElementTree as ET
import numpy as np

PROFILE=np.array([[-.42,.044],[-.38,.046],[-.30,.050],[-.22,.056],[-.14,.062],[-.06,.064],[0,.060],[.065,.052],[.12,.042],[.16,.030],[.181,.025],[.197,.024]],dtype=float)

def radius(z):
    x,y=PROFILE.T; delta=np.diff(y)/np.diff(x)
    slopes=np.zeros(len(x)); slopes[0]=delta[0]; slopes[-1]=delta[-1]
    for i in range(1,len(x)-1):
        if delta[i-1]*delta[i]>0: slopes[i]=2/(1/delta[i-1]+1/delta[i])
    i=max(0,min(len(x)-2,int(np.searchsorted(x,z)-1)))
    h=x[i+1]-x[i]; t=(z-x[i])/h
    r=(2*t**3-3*t*t+1)*y[i]+(t**3-2*t*t+t)*h*slopes[i]+(-2*t**3+3*t*t)*y[i+1]+(t**3-t*t)*h*slopes[i+1]
    d=((6*t*t-6*t)*y[i]+(3*t*t-4*t+1)*h*slopes[i]+(-6*t*t+6*t)*y[i+1]+(3*t*t-2*t)*h*slopes[i+1])/h
    return r,d

def surface(path,z0,z1,phi0,phi1,offset=0,nz=80,na=128):
    vertices=[]; normals=[]; faces=[]
    for z in np.linspace(z0,z1,nz+1):
        r,slope=radius(z); r+=offset
        for phi in np.linspace(phi0,phi1,na+1):
            c,s=math.cos(phi),math.sin(phi)
            vertices.append((r*c,r*s,z))
            n=np.array([c,s,-slope]); n/=np.linalg.norm(n)
            normals.append(n)
    def index(i,j): return i*(na+1)+j+1
    for i in range(nz):
        for j in range(na): faces.append((index(i,j),index(i,j+1),index(i+1,j+1),index(i+1,j)))
    # Add end caps to the complete shell. Partial panels remain curved surfaces.
    if abs(phi1-phi0-2*math.pi)<1e-6:
        for row,z,sign in [(0,z0,-1),(nz,z1,1)]:
            center=len(vertices)+1; vertices.append((0,0,z)); normals.append((0,0,sign))
            for j in range(na):
                tri=(center,index(row,j),index(row,j+1))
                faces.append(tri if sign>0 else tri[::-1])
    with path.open('w',encoding='ascii') as f:
        f.write('# Authored smooth forearm geometry for the homepage animation.\n')
        for v in vertices: f.write('v '+' '.join(f'{x:.8f}' for x in v)+'\n')
        for n in normals: f.write('vn '+' '.join(f'{x:.8f}' for x in n)+'\n')
        for face in faces: f.write('f '+' '.join(f'{i}//{i}' for i in face)+'\n')

def install(xml,assets_dir):
    asset=xml.find('asset'); arm=xml.find('.//body[@name="rh_forearm"]')
    wrist=xml.find('.//body[@name="rh_wrist"]')
    palm=xml.find('.//body[@name="rh_palm"]')
    for body in (arm,wrist):
        for geom in list(body.findall('geom')):
            if geom.get('class')=='plastic_visual': body.remove(geom)
    for name,color,spec,shine in [
        ('arm_shell','.21 .23 .25 1','.75','.45'),
        ('arm_panel','.10 .12 .14 1','.65','.60'),
        ('arm_titanium','.54 .57 .60 1','.95','.85'),
        ('arm_dark','.035 .043 .051 1','.45','.35')]:
        ET.SubElement(asset,'material',name=name,rgba=color,specular=spec,shininess=shine)
    def geom(parent,**attrs):
        return ET.SubElement(parent,'geom',group='2',contype='0',conaffinity='0',**{k:str(v) for k,v in attrs.items()})
    def mesh(name,z0,z1,phi0=0,phi1=2*math.pi,offset=0,material='arm_shell',nz=80,na=128):
        path=assets_dir/(name+'.obj'); surface(path,z0,z1,phi0,phi1,offset,nz,na)
        ET.SubElement(asset,'mesh',name=name,file=path.name,scale='1 1 1',maxhullvert='64')
        geom(arm,type='mesh',mesh=name,material=material)
    mesh('precision_shell',-.42,.197)
    # Curved inset panels with slim metal edges, rather than a broad faceted block.
    for side,phi in enumerate([-math.pi/2,math.pi/2]):
        mesh(f'precision_panel_{side}',-.20,.116,phi-.52,phi+.52,.0008,'arm_panel',64,32)
        for edge in [-1,1]:
            p=phi+edge*.52
            mesh(f'precision_panel_edge_{side}_{edge}',-.20,.116,p-.007,p+.007,.0012,'arm_titanium',64,2)
        for vent,z in enumerate([-.105,-.080,-.055,-.030,-.005]):
            mesh(f'precision_vent_{side}_{vent}',z-.002,z+.002,phi-.31,phi+.31,.0014,'arm_dark',2,24)
        for z in [-.184,.102]:
            for p in [phi-.43,phi+.43]:
                r,_=radius(z); r+=.002
                q=f'{math.sqrt(.5)} {-math.sin(p)*math.sqrt(.5)} {math.cos(p)*math.sqrt(.5)} 0'
                geom(arm,type='cylinder',pos=f'{r*math.cos(p)} {r*math.sin(p)} {z}',size='.0024 .001',quat=q,material='arm_titanium')
    # Turned rings, seams and the tapered bearing housing at the wrist.
    for n,(z,half,mat) in enumerate([(-.215,.003,'arm_titanium'),(.12,.002,'arm_dark'),(.173,.004,'arm_titanium'),(.188,.002,'arm_dark')]):
        mesh(f'precision_ring_{n}',z-half,z+half,offset=.0007,material=mat,nz=4)
    geom(arm,type='cylinder',pos='0 0 .204',size='.024 .007',material='arm_dark')
    geom(arm,type='cylinder',pos='0 0 .211',size='.020 .004',material='arm_titanium')
    # Two actual wrist axes: a transverse bearing, paired yoke rails, and the
    # second pivot directly before the original palm. Hardware follows the rig.
    geom(wrist,type='cylinder',pos='0 0 .005',size='.016 .027',quat='.7071068 .7071068 0 0',material='arm_titanium')
    for side in [-1,1]:
        geom(wrist,type='cylinder',pos=f'0 {side*.027} .005',size='.011 .002',quat='.7071068 .7071068 0 0',material='arm_dark')
        geom(wrist,type='cylinder',pos=f'0 {side*.029} .005',size='.0045 .0015',quat='.7071068 .7071068 0 0',material='arm_titanium')
        geom(wrist,type='box',pos=f'0 {side*.0306} .005',size='.0028 .0002 .00045',material='arm_dark')
        geom(wrist,type='capsule',fromto=f'{side*.020} 0 .007 {side*.020} 0 .033',size='.0055',material='arm_titanium')
        geom(wrist,type='cylinder',pos=f'{side*.025} 0 .034',size='.012 .005',quat='.7071068 0 .7071068 0',material='arm_titanium')
        geom(wrist,type='cylinder',pos=f'{side*.031} 0 .034',size='.007 .0015',quat='.7071068 0 .7071068 0',material='arm_dark')
    geom(palm,type='cylinder',pos='0 0 0',size='.010 .023',quat='.7071068 0 .7071068 0',material='arm_dark')
