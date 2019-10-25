import os.path as path
print ''
sep = "#"*50 + "\n"
p = "/jobs/ads/visa_debit_holidays_J603518/VDH/sh003/m_003/images/VDH_sh003_lighting_lighting_v005/"
print "{0}SEARCHING FOR BAD FILES IN: {1}\n{0}".format(sep,p)


files = [f for f in os.listdir(p) if path.isfile(path.join(p,f))]
bad_files = [x for x in files if path.getsize(path.join(p,x)) < 1000]
bad_files = sorted(bad_files)
for f in bad_files:
	print "{} is a bad file with size {}".format(f, path.getsize(path.join(p, f)))
print "\n{0}There were {1} bad files out of a total {2} in folder:\n{3}\n{0}".format(sep, len(bad_files), len(files), p)
