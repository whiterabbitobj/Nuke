import os

parser = ArgumentParser()
parser.add_argument("show", nargs='?', type=str)
# parser.add_argument("-ext", type=str)
# parser.add_argument("-rv", action="store_true")
# parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()
show = args.show

shows_list = os.listdir("E:/Google Drive/WORK/MIND_MACHINE/SHOWS")
if show in shows_list:
    os.environ['NUKE_PATH'] = "E:/Google Drive/WORK/MIND_MACHINE/SHOWS/DWG/pipeline/nukescripts"
    os.environ['SHOW'] = show
else:
    print("{} is not a recognized show!")
