import os
import subprocess

dst = r"E:\Google Drive\WORK\MIND_MACHINE\SHOWS\DWG\production\shot\070\005\ref\wfg_070_005_comp_main_v003.mov"
src = r"E:\DATA\DWG_DATA\from_client\20190416-001_submission\070\005\wfg_070_005_comp_main_v003_jb.mov"
#
# os.system('mklink "{}" "{}"'.format(dst, src))

# subprocess.check_call('mklink "{}" "{}"'.format(dst, src), shell=True)

files = {
r"E:\DATA\DWG_DATA\from_client\20190416-001_submission\025\110\wfg_025_110_plate_bg_v001_tpf.mov":
r"E:\Google Drive\WORK\MIND_MACHINE\SHOWS\DWG\production\shot\025\110\ref\wfg_025_110_plate_bg_v001_tpf.mov",

r"E:\DATA\DWG_DATA\from_client\20190416-001_submission\025\110\wfg_025_110_plate_cutref_v001_tpf.mov":
r"E:\Google Drive\WORK\MIND_MACHINE\SHOWS\DWG\production\shot\025\110\ref\wfg_025_110_plate_cutref_v001_tpf.mov",

r"E:\DATA\DWG_DATA\from_client\20190416-001_submission\025\110\wfg_025_110_plate_fg-green_v001_tpf.mov":
r"E:\Google Drive\WORK\MIND_MACHINE\SHOWS\DWG\production\shot\025\110\ref\wfg_025_110_plate_fg-green_v001_tpf.mov"

}

for src, dst in files.items():
    # print(src, dst)
    os.system('mklink "{}" "{}"'.format(dst, src))
    # try:
    #     subprocess.check_call('mklink "{}" "{}"'.format(dst, src), shell=True)
    #     print("Made symlink at: {}".format(dst))
    # except CalledProcessError


datadir = "E:/DATA/DWG_DATA/from_client/20190416-001_submission"
proddir = "E:/Google Drive/WORK/MIND_MACHINE/SHOWS/DWG/production/shot"
print(datadir)

files = {
"/025/110": "/025/110/ref",
"/025/190": "/025/190/ref",
"/025/210": "/025/210/ref",
"/068/010": "/068/010/ref",
"/068/020": "/068/020/ref",
"/068/030": "/068/030/ref",
"/068/040": "/068/040/ref",
"/068/050": "/068/050/ref",
"/068/060": "/068/060/ref",
"/068/090": "/068/090/ref",
"/070/005": "/070/005/ref"
}

for src, dst in files.items():
    # cur_dir = os.path.join(datadir, src)
    cur_dir = datadir + src
    # print(cur_dir)
    for f in os.listdir(cur_dir):
        dstfile = os.path.join(proddir, dst, f)
        srcfile = os.path.join(cur_dir, f)
        os.system('mklink "{}" "{}"'.format(dstfile, srcfile))
        print("Copied {} -> {}".format(srcfile, dstfile))




 print(os.listdir(datadir))
# [wfg_025_110_plate_bg_v001_tpf.mov,wfg_025_110_plate_cutref_v001_tpf.mov,wfg_025_110_plate_fg-green_v001_tpf.mov]
#
#
#
#

# /025/110/wfg_025_110_plate_bg_v001_tpf.mov
# /025/110/wfg_025_110_plate_cutref_v001_tpf.mov
# /025/110/wfg_025_110_plate_fg-green_v001_tpf.mov
#
#
#
# /025/190/wfg_025_190_plate_bg_v001_tpf.mov
# /025/190/wfg_025_190_plate_cutref_v001_tpf.mov
# /025/190/wfg_025_190_plate_fg-green_v001_tpf.mov
# /025/190/wfg_025_190_plate_fg-vlad-seitlich_v001_tpf.mov
#
# /025/210/wfg_025_210_comp_main_v040_jma.mov
# /025/210/wfg_025_210_plate_bg_v001_tpf.mov
# /025/210/wfg_025_210_plate_cutref_v002_tpf.mov
# /025/210/wfg_025_210_plate_fg_v001_tpf.mov

/025/230/wfg_025_230_plate_bg_v001_tpf.mov
/025/230/wfg_025_230_plate_cutref_v001_tpf.mov
/025/230/wfg_025_230_plate_fg-green_v001_tpf.mov

/068/010/wfg_068_010_comp_main_v015_jb.mov
/068/010/wfg_068_010_plate_bg_v001_tpf.mov
/068/010/wfg_068_010_plate_cutref_v002_jwo.mov
/068/010/wfg_068_010_plate_fg_v001_tpf.mov

/068/020/wfg_068_020_comp_main_v028_jb.mov
/068/020/wfg_068_020_plate_bg_v001_tpf.mov
/068/020/wfg_068_020_plate_cutref_v002_tpf.mov
/068/020/wfg_068_020_plate_gf_v001_tpf.mov

/068/030/wfg_068_030_plate_bg_v001_tpf.mov
/068/030/wfg_068_030_plate_cutref_v001_tpf.mov
/068/030/wfg_068_030_plate_fg_v001_tpf.mov

/068/040/wfg_068_040_plate_bg_v001_tpf.mov
/068/040/wfg_068_040_plate_cutref_v001_tpf.mov
/068/040/wfg_068_040_plate_fg_v001_tpf.mov

/068/050/wfg_068_050_plate_bg_v001_tpf.mov
/068/050/wfg_068_050_plate_cutref_v001_tpf.mov
/068/050/wfg_068_050_plate_fg_v001_tpf.mov

/068/060/wfg_068_060_plate_bg_v001_tpf.mov
/068/060/wfg_068_060_plate_cutref_v001_tpf.mov
/068/060/wfg_068_060_plate_fg-green_v001_tpf.mov

/068/090/wfg_068_090_plate_bg_v001_tpf.mov
/068/090/wfg_068_090_plate_cutref_v001_tpf.mov
/068/090/wfg_068_090_plate_fg_v001_tpf.mov

/070/005/wfg_070_005_comp_main_v003_jb.mov
/070/005/wfg_070_005_plate_cutref_v001_tpf.mov
/070/005/wfg_070_005_plate_main_v001_tpf.mov
