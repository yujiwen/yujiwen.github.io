from pathlib import Path
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
import concurrent.futures, subprocess

root=Path(__file__).parent/'shadow-model'
root.mkdir(parents=True,exist_ok=True)
commit='f054586a8e90465d49ee5be15335c4a0c7f57caf'
base=f'https://raw.githubusercontent.com/google-deepmind/mujoco_menagerie/{commit}/shadow_hand/'
def read(url):
    for attempt in range(3):
        try: return urlopen(Request(url+f'?download=1&attempt={attempt}',headers={'Accept-Encoding':'identity'}),timeout=30).read()
        except Exception:
            if attempt==2: raise
for name in ('right_hand.xml','README.md','LICENSE','scene_right.xml'):
    (root/name).write_bytes(read(base+name))
files=[m.get('file') for m in ET.parse(root/'right_hand.xml').findall('./asset/mesh')]
(root/'assets').mkdir(exist_ok=True)
def fetch(name):
    if (root/'assets'/name).exists(): return name,(root/'assets'/name).stat().st_size
    data=read(base+'assets/'+name)
    (root/'assets'/name).write_bytes(data)
    return name,len(data)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    for result in pool.map(fetch,files): print(*result,flush=True)
(root/'REVISION').write_text(commit+'\n',encoding='utf-8')
print('Pinned revision',commit)
