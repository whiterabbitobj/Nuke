
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
	