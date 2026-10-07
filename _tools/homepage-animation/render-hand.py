from pathlib import Path
import sys, math, xml.etree.ElementTree as ET
root=Path(__file__).parent
sys.path.insert(0,str(root/'motion-runtime'))
import mujoco as mj
import numpy as np
from PIL import Image, ImageDraw
import importlib.util
arm_spec=importlib.util.spec_from_file_location('precision_arm',root/'precision-arm.py')
precision_arm=importlib.util.module_from_spec(arm_spec); arm_spec.loader.exec_module(precision_arm)

model_dir=root/'shadow-model'
tree=ET.parse(model_dir/'right_hand.xml'); xml=tree.getroot()
xml.find('compiler').set('meshdir',str(model_dir/'assets'))
xml.find('./worldbody/body').set('pos','-0.32 0 0')
visual=ET.SubElement(xml,'visual')
ET.SubElement(visual,'global',offwidth='1600',offheight='900')
ET.SubElement(visual,'quality',offsamples='4',shadowsize='4096')
ET.SubElement(visual,'headlight',ambient='.36 .35 .34',diffuse='.55 .54 .52',specular='.35 .35 .35')
ET.SubElement(xml.find('asset'),'texture',type='skybox',builtin='gradient',rgb1='.91 .90 .88',rgb2='.96 .95 .93',width='512',height='3072')
world=xml.find('worldbody')
precision_arm.install(xml,model_dir/'assets')
ET.SubElement(world,'light',pos='-.2 -.6 .8',dir='.2 .6 -.8',directional='true',diffuse='.55 .54 .52',specular='.6 .6 .6',castshadow='true')
ET.SubElement(world,'light',pos='.6 .3 .4',dir='-.6 -.3 -.4',directional='true',diffuse='.4 .42 .45',specular='.7 .72 .75',castshadow='false')
for name,rgba,spec in [('black','.11 .12 .13 1','.8'),('gray','.64 .66 .69 1','.85'),('metallic','.78 .80 .83 1','1')]:
    m=xml.find(f"./asset/material[@name='{name}']")
    m.set('rgba',rgba); m.set('specular',spec); m.set('shininess','.65')
model=mj.MjModel.from_xml_string(ET.tostring(xml,encoding='unicode'))
data=mj.MjData(model)
opt=mj.MjvOption(); opt.geomgroup[3:]=0
renderer=mj.Renderer(model,height=900,width=1600)
camera=mj.MjvCamera()
camera.type=mj.mjtCamera.mjCAMERA_FREE
camera.lookat[:]=[-.055,0,.065]
camera.distance=.43
camera.azimuth=100
camera.elevation=-40
index={model.joint(i).name:int(model.jnt_qposadr[i]) for i in range(model.njnt)}

def pose(t):
    data.qpos[:]=0
    for j,prefix in enumerate(['FF','MF','RF','LF']):
        # A single-finger flex, a traveling wave, a two-finger pose, and a
        # staggered release. Each digit gets a distinct continuous trajectory.
        x=(t-.55-j*.68)
        individual=math.sin(math.pi*x/1.35)**2 if 0<x<1.35 else 0
        x=t-4-j*.50
        wave=math.sin(math.pi*x/2.8)**2 if 0<x<2.8 else 0
        x=t-8.2
        hold=math.sin(math.pi*x/4.4)**2 if 0<x<4.4 else 0
        x=t-13.0-j*.25
        release=math.sin(math.pi*x/3.0)**2 if 0<x<3 else 0
        flex=.75*individual+.9*wave+(.10 if j<2 else 1.0)*hold+.62*release
        data.qpos[index[f'rh_{prefix}J3']]=.08+.95*flex
        data.qpos[index[f'rh_{prefix}J2']]=.10+1.02*flex
        data.qpos[index[f'rh_{prefix}J1']]=.07+.72*flex
        # Small, independent abduction while the palm turns.
        data.qpos[index[f'rh_{prefix}J4']]=[-.08,-.02,.035,.10][j]+.025*math.sin(2*math.pi*t/18+j)*math.sin(math.pi*t/18)**2
    data.qpos[index['rh_LFJ5']]=.08*math.sin(math.pi*t/18)**2
    data.qpos[index['rh_THJ5']]=.28+.13*math.sin(2*math.pi*t/18)
    data.qpos[index['rh_THJ4']]=.25+.17*math.sin(math.pi*t/18)**2
    data.qpos[index['rh_THJ3']]=.04*math.sin(2*math.pi*t/18)
    data.qpos[index['rh_THJ2']]=.12+.12*math.sin(math.pi*t/18)**2
    data.qpos[index['rh_THJ1']]=.17+.22*math.sin(math.pi*t/18)**2
    data.qpos[index['rh_WRJ1']]=-.08+.14*math.sin(2*math.pi*t/18)
    data.qpos[index['rh_WRJ2']]=-.15+.10*math.sin(2*math.pi*t/18)
    mj.mj_forward(model,data)

def render(t):
    pose(t); renderer.update_scene(data,camera,scene_option=opt)
    return renderer.render()

if __name__=='__main__':
    sheet=Image.new('RGB',(1200,900))
    for i,t in enumerate([0,1.2,2.1,5.6,10.4,14.3]):
        frame=Image.fromarray(render(t)).resize((600,337))
        ImageDraw.Draw(frame).text((10,10),f'{t}s',fill='black')
        sheet.paste(frame,((i%2)*600,(i//2)*300))
    sheet.save(root/'shadow-views.jpg')
    print('Views rendered',flush=True)
    renderer.close()
