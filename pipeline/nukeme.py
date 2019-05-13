import os
from pathlib import Path
import subprocess

nuke = os.environ['NUKE_VER']
path = Path(os.environ['COMP_PATH'])

files = [file for file in path.rglob('*') if file.suffix == '.nk']
latest = str(sorted(files, key=lambda x: os.path.getmtime(x))[-1])
print("Found {}\n\n    Loading...\n".format(latest))
sys_command = '"{}" "{}"'.format(nuke, latest)
subprocess.Popen([nuke, latest])
