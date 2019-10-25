import os
import nuke

sep = "#"*30
print(sep)
# Import NODES/PLUGINS in init.py
facility_plugins = "/mill3d/users/dollm/Nuke/nodes"
nuke.pluginAddPath(facility_plugins)
print("Loading nodes from " + facility_plugins)

# Load show-specific init.py/menu.py
try:
	show_path = os.environ['SHOW_PATH']
	show_path = os.path.join(show_path, 'pipeline', 'nuke')
	if os.path.isdir(show_path):
		print("Loading custom configs from " + show_path.replace('\\','/'))
		nuke.pluginAddPath(show_path)
except:
	print("Could not load a show-based plugin repository.")
print(sep)


# Implement callbacks

#def writeNodeDirs():
#	import os, nuke
#	file = nuke.filename(nuke.thisNode())
#	dir = os.path.dirname(file)
#	# osdir = nuke.callbacks.filenameFilter(dir)
#	try:
#		# os.makedirs(osdir)
#		os.makedirs(dir)
#	except OSError:
#		pass

#nuke.addBeforeRender(writeNodeDirs)
