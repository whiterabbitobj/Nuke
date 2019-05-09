
def deSel():
	for node in nuke.selectedNodes():
		node['selected'].setValue(False)
	return



