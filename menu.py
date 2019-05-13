import os

################################################################################
# Add custom scripts/plugins
################################################################################

# importing all scripts from the scrips folder, as a module, and batch importing
# this is bad form, against PEP, etc... but too handy and low risk for this app
# from scripts import *
#
#
import scripts

# Adds file handling functionality from dragAndDrop.py
# (must exist in the .../REPO/nukescripts folder!)

### !!! CURRENTLY THIS SCRIPT BUGS OUT COPY/PASTA. DISABLED UNTIL FURTHER
### !!! DEBUGGING CAN BE DONE
# nukescripts.drop.addDropDataCallback(scripts.fileHandler)
# nukescripts.drop.addDropDataCallback(scripts.pathHandler)
# nukescripts.drop.addDropDataCallback(scripts.dropHandler)


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

# nuke.knobDefault('Write.raw', 'True')
nuke.knobDefault('Write.file', '[getenv RENDER_PATH]/[value root.rootname]/exr/[value root.rootname]_mdo.%04d.exr')
nuke.knobDefault('Write.label', '[value file]')
nuke.knobDefault('Write.channels', 'rgba')
nuke.knobDefault('Write.compression', 'dwaa')

# nuke.knobDefault('Read.raw', 'True')
nuke.knobDefault('Read.label', '[value width]x[value height]')



################################################################################
# Add custom menus/aliases
################################################################################

m = nuke.menu("Nuke").addMenu("&Mind:Machine")

# m.addCommand("Render selected", "renderThis(nuke.selectedNodes('Write'))")
# m.addCommand("RV selected", "rvFinalCheck(nuke.selectedNodes('Read'))", "Alt+r")

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


n.addCommand('Align to axis', "scripts.alignNodes()", 'Alt+l')
#n.addCommand('Publish this shot', "publishThisShot(nuke.selectedNode())", 'Alt+p')
n.addCommand('Open Viewer Input', "nuke.show(nuke.toNode('VIEWER_INPUT'))", 'Alt+v')
n.addCommand('Create Read from Write', "scripts.readFromWrite()", 'Alt+r')

#n.addCommand('Create Precomp setup', "dollPcompCreate()", 'Alt+p')
#n.addCommand('Make hero links', 'makeHeroLinks(nuke.selectedNode())', 'Alt+h')
