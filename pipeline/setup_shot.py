import os
from argparse import ArgumentParser


# Collect command line arguments
parser = ArgumentParser()
parser.add_argument("-path", type=str, default=os.getcwd())
parser.add_argument("shotname", nargs='?', type=str)
# parser.add_argument("-ext", type=str)
# parser.add_argument("-rv", action="store_true")
# parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()
shotname = args.shotname

print("CREATING SHOT: {}".format(shotname))
# path = args.path
# ext = args.ext
# do_rv = args.rv
# concise = not args.verbose
