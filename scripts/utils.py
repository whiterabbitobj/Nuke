import re
import os
import nuke

def refreshAllReads():
    for node in nuke.allNodes("Read"):
    	node['reload'].execute()
def rar():
	refreshAllReads()
def refreshreads():
	refreshAllReads()
def refreshallreads():
	refreshAllReads()



def deSel():
	for node in nuke.selectedNodes():
		node['selected'].setValue(False)
	return



def relabelIt(selNode):

	new = "Label: "
	size = "Size: "
	p   = nuke.Panel("Relabel")
	nl  = selNode['label']
	ns  = selNode['note_font_size']

	curLabel = nl.value()
	curSize  = int(ns.value())

	p.addSingleLineInput(new,curLabel)
	p.addSingleLineInput(size,curSize)

	p.show()

	newLabel = p.value(new)
	newSize  = int(p.value(size))

	nl.setValue(newLabel)
	ns.setValue(newSize)
	return



def centerOnTarget(selNode):
    for node in nuke.selectedNodes():
        node['selected'].setValue(0)
    selNode['selected'].setValue(True)
    x = selNode['xpos'].value()
    y = selNode['ypos'].value()
    nuke.zoom(1,(x,y))
    selNode['selected'].setValue(False)


def readFromWrite():
    nodes = nuke.selectedNodes()
    for node in nodes:
        assert node.Class() == 'Write'
        filename = nuke.filename(node)

        while True:
            dir = os.path.dirname(filename)
            print("Looking for:", filename)

            try:
                fileset = nuke.getFileNameList(dir)[0]
                print("Found fileset on disk: ", fileset)
                break
            except:
                print("Version not found, searching for previous takes.")
                prefix, num = re.search(r'(v)(\d+)', filename,
                                        re.IGNORECASE).groups()
                new_ver = str(int(num) - 1).zfill(len(num))
                assert int(new_ver) > 0, "NO VERSIONS FOUND"
                filename = re.sub(r'v(\d+)', prefix + new_ver, filename)

        fileset = os.path.join(dir, fileset)
        read = nuke.createNode('Read')
        read['file'].fromUserText(fileset)
        read.setXYpos(node.xpos(), node.ypos() + 120)


def splayLayers(n):
	x = n.xpos()
	y = n.ypos() + 100
	layers = list( set( [c.split('.')[0] for c in n.channels()] ) )
	layers = sorted(layers, key=lambda x: x.lower())

	d0 = nuke.createNode("Dot")
	d0.setXYpos(x, y)
	d0.setInput(0, n)

	for layer in layers:
		d = nuke.createNode("Dot")
		d.setXYpos(x, y)
		s = nuke.createNode("Shuffle", 'label {0} in {0}'.format(layer))
		s.setXYpos(x-25, y+150)
		x += 150
		d.setInput(0, d0)
		s.setInput(0, d)
		d0 = d
