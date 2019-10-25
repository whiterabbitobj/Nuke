import os.path as path

old = "/jobs/ads/visa_debit_holidays_J603518/VDH/sh001/m_001/images/VDH_sh001_lighting_lighting_v001/VDH_sh001_lighting_lighting_v001"
new = "/jobs/ads/visa_debit_holidays_J603518/VDH/sh002/m_002/images/VDH_sh002_lighting_lighting_v001/VDH_sh002_lighting_lighting_v001"
newdir = path.dirname(new)
files = [path.join(newdir, f) for f in nuke.getFileNameList(newdir)]


for read in nuke.allNodes("Read"):
    r1 = nuke.filename(read).split('.')[0]
    r2 = r1.replace(old, new)

	for f in files:
		if f.startswith(r2):
			read['file'].fromUserText(f)
			print "\n{} ...updated to:\n{}".format(r1, f)
			break

