import os
from argparse import ArgumentParser


# Collect command line arguments
parser = ArgumentParser()
parser.add_argument("-path", type=str, default=os.getcwd())
parser.add_argument("shot", nargs="+", type=str)
#parser.add_argument("shot", type=str)



args = parser.parse_args()
# seq = args.seq
shot = args.shot

if len(shot) == 1:
    shot = shot[0].split('_')

assert len(shot)==2, "Incorrect format. Please use format SEQ_SHOT or SEQ SHOT."

seq = shot[0]
shot = shot[1]

assert len(seq)==3 and len(shot)==3, "SEQ or SHOT should be 3 digits!"

show = os.environ['SHOW']
show_path = os.environ['SHOW_PATH']
shotname =  "{}_{}_{}".format(show, seq, shot)

print("CREATING SHOT: {}".format(shotname))

standard_loc = os.path.join("pipeline", "file_structure")
shots_loc = os.path.join("production", "shot")
dir_structure = os.walk(os.path.join(show_path, standard_loc))

for root, dirs, files in dir_structure:
    # print(root, dir, files)
    for dir in dirs:
        dir = os.path.join(root, dir)
        fp = dir.replace(standard_loc, shots_loc)
        fp = fp.replace("SEQ", seq)
        fp = fp.replace("SHOT", shot)
        fp = fp.replace("\\", "/")
        try:
            os.makedirs(fp)
            print("Created directory: ", fp)
        except OSError:
            print("... not created: {} (ALREADY EXISTS)".format(fp))
        except:
            print("Could not create directory: ", fp)
            pass
    # Below code is not implemented until/unless standard files need to be copied.
    for file in files:
        pass
