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
