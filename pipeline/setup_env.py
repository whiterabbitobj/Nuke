import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("show", nargs='?', type=str)

args = parser.parse_args()
show = args.show

shows_list = os.listdir("E:/Google Drive/WORK/MIND_MACHINE/SHOWS")
if show in shows_list:
    os.environ['NUKE_PATH'] = "E:/Google Drive/WORK/MIND_MACHINE/SHOWS/DWG/pipeline/nukescripts"
    os.environ['SHOW'] = show
    for i in os.environ:
        print(i)
else:
    print("{} is not a recognized show!")
