import os
import os.path

import glob
import pyseq

p = "E:/die_wolf_gang/20190503-003_Submission/localized/8001001409/008/010/output/comp/main/pre/MatpPrep/v002/3424x2202_exr/wfg_008_010_comp_main_pre_MatpPrep_v002_jb.1100.exr"


o = "E:/die_wolf_gang/20190503-003_Submission/localized/8001001409"


# print(os.path.basename(p))
#
#
# for fp in glob.glob(os.path.join(o, "**/*.exr"), recursive=True):
#     print(fp)
#
#
# import pyseq
#
#
# seqs = pyseq.get_sequences(p + '*')
# print(seqs)
#
# for s in seqs:
#     print(s)
#
#
# glob.glob(o + "/**/*", recursive=True)
#

#
# dirs = set([root for root, _, _ in os.walk(o)])
# seq_list = []
# for d in dirs:
#     for s in pyseq.get_sequences(d):
#         seq_list.append(s)
#
# for s in seq_list:
#     print(s)


path = "E:/DATA/die_wolf-gang_DATA/from_client"

for r, d, f in pyseq.walk(path):
    print(f)
