# Homepage finger animation

This folder preserves the authored finger and wrist trajectories. It is excluded
from Jekyll output by its leading underscore. The website plays the small rendered
MP4 files; no 3D library is downloaded or executed by visitors.

From this directory, in a Python 3.11+ environment:

```
python -m pip install -r requirements.txt
python fetch-shadow.py
python export-dexterous.py
```

The downloader fetches the Apache-2.0 Shadow Hand model at the pinned Menagerie
revision. Downloads and intermediate exports are ignored by Git. The exporter
checks joint limits, digit independence, the loop pose seam and full video decode,
then copies desktop/mobile video and the still to `assets/videos/`.

`render-hand.py` defines the motions in `pose(t)`, including staggered flexion,
traveling waves, contrasting finger combinations and wrist movement. It also
contains lighting, materials, camera and the additional arm geometry. Running
that script alone produces a contact sheet for visual inspection.

`precision-arm.py` creates the smooth, tapered forearm, inset panels, vents,
turned collars, fasteners and wrist hardware. It replaces the model's original
forearm and wrist visual meshes while retaining the original hand rig and the
accepted 18-second finger/thumb/wrist animation. Outputs use the `robot-precision`
filename prefix; the previous `robot-dexterous` exports are preserved.

Source attribution and the full model license are retained in
`assets/videos/robot-dexterous-NOTICE.txt` and
`docs/third-party/shadow-hand-LICENSE.txt`.
