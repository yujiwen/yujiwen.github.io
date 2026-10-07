from pathlib import Path
import subprocess, shutil, importlib.util
root=Path(__file__).parent
spec=importlib.util.spec_from_file_location('hand',root/'render-hand.py')
hand=importlib.util.module_from_spec(spec); spec.loader.exec_module(hand)
ff=shutil.which('ffmpeg') or __import__('imageio_ffmpeg').get_ffmpeg_exe()
out=root/'robot-precision'; out.mkdir(exist_ok=True)
repo=root.parents[1]
fps=24; duration=18

# Verify the authored animation rather than relying on video playback alone.
hand.pose(0); start=hand.data.qpos.copy()
hand.pose(duration)
assert hand.np.max(hand.np.abs(hand.data.qpos-start))<1e-10, 'Loop pose seam'
for t in hand.np.linspace(0,duration,721):
    hand.pose(float(t))
    for joint in range(hand.model.njnt):
        value=hand.data.qpos[hand.model.jnt_qposadr[joint]]
        low,high=hand.model.jnt_range[joint]
        assert hand.np.isfinite(value) and low-1e-8<=value<=high+1e-8, (t,joint,value)
hand.pose(2.1)
flex=[hand.data.qpos[hand.index[f'rh_{p}J3']] for p in ('FF','MF','RF','LF')]
assert max(flex)-min(flex)>.4, 'Digits must move independently'
print('Loop seam, all joint ranges, and independent digit trajectories passed',flush=True)

target=out/'robot-precision-loop.mp4'
process=subprocess.Popen([ff,'-v','error','-f','rawvideo','-pix_fmt','rgb24','-s','1600x900','-r',str(fps),'-i','pipe:0','-an','-c:v','libx264','-preset','medium','-crf','24','-pix_fmt','yuv420p','-movflags','+faststart','-y',str(target)],stdin=subprocess.PIPE)
try:
    for frame in range(fps*duration):
        process.stdin.write(hand.render(frame/fps).tobytes())
        if frame%72==0: print('Rendered',frame,'/',fps*duration,flush=True)
    process.stdin.close()
    if process.wait()!=0: raise RuntimeError('Video encoder failed')
    hand.Image.fromarray(hand.render(5.6)).save(out/'robot-precision-poster.jpg',quality=93)
finally:
    hand.renderer.close()
subprocess.run([ff,'-v','error','-i',str(target),'-vf','scale=1100:618:flags=lanczos','-an','-c:v','libx264','-preset','slow','-crf','26','-pix_fmt','yuv420p','-movflags','+faststart','-y',str(out/'robot-precision-loop-sm.mp4')],check=True)
for path in out.glob('*.mp4'):
    result=subprocess.run([ff,'-v','error','-i',str(path),'-f','null','-'],capture_output=True,check=True)
    assert not result.stderr, result.stderr
for path in out.iterdir():
    shutil.copy2(path,repo/'assets'/'videos'/path.name)
    print(path.name,path.stat().st_size,flush=True)
