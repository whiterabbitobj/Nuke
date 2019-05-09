import os

################################################################################
# Add custom scripts/plugins
################################################################################
facility_scripts = "E:/Google Drive/WORK/VFX/Nuke/REPO/nukescripts"

# nuke.pluginAddPath(facility_scripts)
for file in os.listdir(facility_scripts):
	if file.endswidth(".py"):
		from file import *

# Adds file handling functionality from dragAndDrop.py
# (must exist in the .../REPO/nukescripts folder!)
nukescripts.drop.addDropDataCallback(fileHandler)
nukescripts.drop.addDropDataCallback(pathHandler)
nukescripts.drop.addDropDataCallback(dropHandler)


################################################################################
# Setup node defaults
################################################################################

nuke.knobDefault('RotoPaint.cliptype', 'no clip')
nuke.knobDefault('RotoPaint.output', 'alpha')

nuke.knobDefault('Roto.cliptype', 'no clip')
nuke.knobDefault('Roto.output', 'alpha')

nuke.knobDefault('Shuffle.label', '[value in]')


nuke.knobDefault('Invert.channels', 'alpha')
nuke.knobDefault('Clamp.channels', 'alpha')


nuke.knobDefault('Dot.note_font_size', '22')
nuke.knobDefault('Dot.note_font_color', '4278190335')
nuke.knobDefault('Dot.note_font', 'Bitstream Vera Sans Italic')

nuke.knobDefault('Merge2.note_font_size', '13')
nuke.knobDefault('Merge2.note_font_color', '16711935')
nuke.knobDefault('Merge2.note_font', 'Bitstream Vera Sans Bold')

nuke.knobDefault('Write.raw', 'True')
nuke.knobDefault('Read.raw', 'True')


################################################################################
# Add custom menus/aliases
################################################################################

m = nuke.menu("Nuke").addMenu("&Mind:Machine")

m.addCommand("Render selected", "renderThis(nuke.selectedNodes('Write'))")
m.addCommand("RV selected", "rvFinalCheck(nuke.selectedNodes('Read'))", "Alt+r")

# Create a dictionary of aliases and the node class they reference to
nodeAliases = {
    "Lookup"   : "ColorLookup",
    "Spline"   : "Bezier",
    "Grad"     : "Ramp",
	"Keep"     : "Remove",
	"Lumakey"  : "Keyer",
	"Channels" : "Shuffle"

}

# Build all menu entries for your aliased nodes
n = nuke.menu("Nodes").addMenu("Other/Aliased nodes")
for a,i in nodeAliases.items():
  s = a.upper()
  p = n.addMenu(s[0])
  p.addCommand(a, "nuke.createNode('"+i+"')")


n.addCommand('Align to axis', "dollAlignNodes()", 'Alt+l')
#n.addCommand('Publish this shot', "publishThisShot(nuke.selectedNode())", 'Alt+p')
n.addCommand('Open vIP', "nuke.show(nuke.toNode('vIP'))", 'Alt+v')
#n.addCommand('Create Precomp setup', "dollPcompCreate()", 'Alt+p')
#n.addCommand('Make hero links', 'makeHeroLinks(nuke.selectedNode())', 'Alt+h')
