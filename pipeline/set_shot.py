from pathlib import Path
import os


work_path = Path(os.environ['WORK_PATH'])
dirs = [i for i in work_path.iterdir() if i.is_dir()]
for dir in dirs:
    print("..{}".format(dir.relative_to(work_path)))
    subdirs = [i for i in dir.iterdir() if i.is_dir()]

    for subdir in subdirs:
        print("....{}".format(subdir.relative_to(work_path / dir)))
