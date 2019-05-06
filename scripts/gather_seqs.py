import os
# import os.path
import pyseq
import subprocess
from argparse import ArgumentParser

def get_seqs(path, ext=""):
    dirs = [[root, subdirs] for root, subdirs, _ in os.walk(path)]
    seq_list = []
    for root, subdirs in dirs:
        sets = pyseq.get_sequences(root + '/*' + ext)
        if len(sets) == 1:
            print(type(sets[0].))
        if subdirs and not sets:
            continue
        print("\nFilesets found in {}:".format(root))
        if  not sets:
            print("EMPTY DIRECTORY!!!")
        for s in sets:
            print("---> {}".format(s))
            seq_list.append(os.path.join(root,s.format('%h#%t')).replace('\\', '/'))
    return seq_list


parser = ArgumentParser()
parser.add_argument("path", nargs='?', type=str, default=os.getcwd())
parser.add_argument("-ext", type=str)
parser.add_argument("-rv", action="store_true")
args = parser.parse_args()
path = args.path
ext = args.ext
do_rv = args.rv


print("Collecting image sequences from: {}".format(path))


seqs = get_seqs(path)
if do_rv:
    subprocess.Popen('E:/Software/rv-win64-x86-64-6.2.3/bin/rv.exe {}'.format(' '.join(get_seqs(path))))
