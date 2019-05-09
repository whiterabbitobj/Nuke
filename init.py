import os


# Import NODES/PLUGINS in init.py
nuke.pluginAddPath("E:/Google Drive/WORK/VFX/Nuke/REPO/nodes")

# Load show-specific init.py/menu.py
show_path = os.environ['SHOW_PATH']
show_path = os.path.join(show_path, 'pipeline', 'nuke')
if os.path.isdir(show_path):
	nuke.pluginAddPath(show_path)


# Other imports happen in menu.py for GUI-loading only