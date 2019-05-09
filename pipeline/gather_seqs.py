import os
import pyseq
import subprocess
from argparse import ArgumentParser
import glob

### THIS SCRIPT WILL USE THE 'PYSEQ' MODULE TO COLLECT AND SUCCINCTLY PRINT
### ALL FILESETS LOCATED UNDER EITHER THE CURRENT (DEFAULT) OR PROVIDED PATH


# Recursively collect filsets below provided directory
def get_seqs(path, ext="", concise=True, short_links=False):
    if not concise:
        num = len(glob.glob(path + "/**/*", recursive=True))
        print("Total files to search: {}".format(num))
    seq_list = []
    for root, dirs, seq in pyseq.walk(path):
        root = root.replace('\\', '/')
        if seq:
            if not concise:
                print("\nFilesets found in ({}):".format(root))
            for s in seq:
                if concise:
                    spath = s.path()
                    if short_links:
                        spath = spath.replace(path,'...')[1:]
                    print(spath.replace('\\','/'))

                else:
                    print("---> {}".format(s))
                if len(s) > 1:
                    s = s.format('%h#%t')
                seq_list.append(os.path.join(root, str(s)))
        elif not dirs:
            print("\n***WARNING***")
            print("FOUND AN EMPTY BOTTOM-LEVEL DIRECTORY! ({})\n".format(root))
    return seq_list


# Collect command line arguments
parser = ArgumentParser()
parser.add_argument("path", nargs='?', type=str, default=os.getcwd())
parser.add_argument("-ext", type=str)
parser.add_argument("-rv", action="store_true")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-rel", "--relative", action="store_true")
parser.add_argument("--do_cd", action="store_true")


args = parser.parse_args()
path = args.path
ext = args.ext
do_rv = args.rv
short_links = args.relative
concise = not args.verbose


# Work with the collected sequences
if args.do_cd:
    get_seqs(path, ext, short_links=True)
    quit()

print("Collecting image sequences from: {}".format(path))

seqs = get_seqs(path, ext, concise, short_links)
print("\n\n...found {} file(set)s.".format(len(seqs)))
if do_rv:
    print("Opening RV...")
    subprocess.Popen('E:/Software/rv-win64-x86-64-6.2.3/bin/rv.exe {}'.format(' '.join(seqs)))
