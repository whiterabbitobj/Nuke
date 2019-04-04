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

###########################
###########################
##                       ##
## DOLL CUSTOM FUNCTIONS ##
##                       ##
###########################
###########################

def refreshAllReads():
    for node in nuke.allNodes("Read"):
    	node['reload'].execute()
	
def rar():
	refreshAllReads()
def refreshreads():
	refreshAllReads()
def refreshallreads():
	refreshAllReads()	

########################

def centerOnTarget(selNode):
    for node in nuke.selectedNodes():
        node['selected'].setValue(0)
    selNode['selected'].setValue(True)
    x = selNode['xpos'].value()
    y = selNode['ypos'].value()
    nuke.zoom(1,(x,y))
    selNode['selected'].setValue(False)

########################

def deSel():
	for node in nuke.selectedNodes():
		node['selected'].setValue(False)
	return
	
########################	

def dollPcompCreate():
	####################
	# should we proceed?
	####################
	if len(nuke.selectedNodes()) >  1:
		nuke.message("Please only select one (1) node.")
		return
	if len(nuke.selectedNodes()) <  1:
		nuke.message("Please select a node.")
		return		
		
	##############################################
	# save selection for later when creating knobs
	##############################################
	selection = nuke.selectedNode() 
	
	########################
	# check for control node ==> in the future this will create one if it doesn't yet exist
	########################
	if not dollCtrlsExists():
		return		
		
	##################		
	# get new filename	
	##################
	newName = dollPcompPrompt()
	if newName == None:
		return
		
	######################
	# create control knobs
	######################		
	if not dollPcompKnobs(newName):
		return
	
	####################
	# create pcomp nodes
	####################
	deSel()
	selection['selected'].setValue(True)
	dollPcompNodes(newName)


########################

def dollPcompKnobs(newName):
	ctrls = nuke.toNode("COMP_CONTROLS")
	pcompList = ["-"]
	
	################################################
	# figure out where the precomp node knobs are at
	################################################
	startIndex = endIndex = 0
	for i in range(ctrls.numKnobs()):
		try:
			if ctrls.knob(i).name() == "pcompGroup":
				startIndex = i+1
			if ctrls.knob(i).name() == "endPcompGroup":
				endIndex = i
		except:
			pass
	if startIndex == 0:
		nuke.message("Precomp group not found.")
		return False
	print "startIndex, endIndex", startIndex, endIndex
			
	###########################################			
	# generate pulldown list of existing pcomps
	###########################################	
	for i in range(startIndex, endIndex):
		if ctrls.knob(i).name().startswith("py_"):
			pcompList.append(ctrls.knob(i).label())
	pcompList = '" "'.join(pcompList)
	pcompList = '"'+ pcompList + '"'
	
	####################################
	# prompt user where to put new pcomp
	####################################
	p = nuke.Panel("Current Precomps")
	listName = "After which existing precomp do you wish to insert the new controls?"
	p.addEnumerationPulldown(listName, pcompList)
	success = p.show()
	if not success:
		nuke.message("You have not chosen a place to insert the new knobs. Aborting...")
		return False
	
	insertHere = "-"
	for knob in ctrls.knobs():
		if ctrls[knob].label() == p.value(listName):
			insertHere = ctrls[knob].name()

	print "Will insert after: " + insertHere
	
	################################
	# create new pcomp control knobs
	################################
	deSel()
	print "Creating Knobs..."
	newCtrls = nuke.createNode("NoOp", inpanel = False)
	for i in range(ctrls.numKnobs()):
		knobName = ctrls.knob(i).name()
		if knobName == "":
			d = nuke.Text_Knob("div" + str(i), "")
			newCtrls.addKnob(d)
			pass
		val = ctrls[knobName].toScript()
		try:
			newCtrls[knobName].fromScript(val)
		except:
			#k = newCtrls.addKnob(ctrls[knobName])
			newCtrls.addKnob(ctrls[knobName])
			if (knobName == insertHere) or ((insertHere == "-") and (knobName == "pcompGroup")):
				wName = "write" + newName
				rName = "read" + newName
				pName = "py_" + newName
				write = nuke.Boolean_Knob(wName)
				read = nuke.Boolean_Knob(rName)
				py = nuke.PyScript_Knob(pName)
				
				newCtrls.addKnob(write)
				newCtrls.addKnob(read)
				newCtrls.addKnob(py)
				
				newCtrls[wName].setLabel("Write")
				newCtrls[wName].setValue(True)
				newCtrls[wName].setFlag(0x1000)
								
				newCtrls[rName].setLabel("Read")
				newCtrls[rName].clearFlag(0x1000)
								
				newCtrls[pName].setLabel("::: " + newName)
				newCtrls[pName].clearFlag(0x1000)
				newCtrls[pName].setCommand("centerOnTarget(nuke.toNode('w_" + newName + "'))")



	##########################
	# remove old controls node
	##########################
	deSel()
	ctrls['selected'].setValue(True)
	#ctrls['name'].setValue("dummyXIJWL")
	nuke.nodeDelete()
	return True
	

########################

def dollCtrlsExists():
	if nuke.toNode("COMP_CONTROLS") == "None":
		nuke.message("There is no COMP_CONTROLS node in this script! Aborting...")
		return False
	return True

########################
	
def dollPcompPrompt():
	##################
	# get new filename
	##################
	p = nuke.Panel("New Filename")
	new = "Enter the filename for the new precomp:"
	p.addSingleLineInput(new,"")
	success = p.show()
	if not success:
		nuke.message("No filename chosen. Aborting...")
		return None
	newName = p.value(new)
	return newName	

########################
	
def dollPcompNodes(newName):

	print "Creating nodes..."
		
	#################
	# set master node
	#################
	mnode = nuke.selectedNode()

	################
	# get pcomp path
	################
	ppath = nuke.root().name()
	ppath = ppath.split('/')
	ppath = '/'.join(ppath[:-2])
	ppath += "/elem/pcomp/"
	
	###########
	# VARIABLES
	###########
	pfile = ppath + newName + ".%d.exr"
	expr = "!parent.COMP_CONTROLS."
		
	######################
	# get master node data
	######################
	xPos = mnode['xpos'].value()
	yPos = mnode['ypos'].value()
	
	##################
	# create DUMMY dot
	##################
	dummy = nuke.createNode("Dot", inpanel = False)
	dummy['ypos'].setValue(yPos + 200)
	deSel()
	mnode['selected'].setValue(True)

	############
	# create dot
	############
	dot = nuke.createNode("Dot", inpanel = False)
	dot['name'].setValue("dot" + newName)
	dot['ypos'].setValue(yPos + 50)
	
	#############
	# create crop
	#############
	crop = nuke.createNode("Crop", inpanel = False)
	crop['name'].setValue("crop" + newName)
		
	##############
	# create write
	##############
	write = nuke.createNode("Write", inpanel = False)
	write['name'].setValue("w_" + newName)	
	write['file'].setValue(pfile)
	write['disable'].setExpression(expr + "write" + newName)
	write['ypos'].setValue(yPos + 100)
	write['xpos'].setValue(xPos - 100)


	deSel()

	#############
	# create read
	#############
	read = nuke.createNode("Read", inpanel = False)
	read['name'].setValue("r_" + newName)	
	read['file'].setValue(pfile)
	read['ypos'].setValue(yPos + 100)
	read['xpos'].setValue(xPos + 100)
	read['first'].setValue(nuke.root()['first_frame'].value())
	read['last'].setValue(nuke.root()['last_frame'].value())
	
	deSel()

	###############
	# create switch
	###############
	switch = nuke.createNode("Switch", inpanel = False)
	switch['name'].setValue("switch_" + newName)	
	switch['which'].setExpression(expr + "read" + newName)
	#switch['ypos'].setValue(yPos + 200)
	#switch['xpos'].setValue(crop['xpos'].value())
	switch.setXpos(xPos)
	switch.setYpos(yPos + 200)
	switch.setInput(0, read)
	switch.setInput(1, crop)

	###################################
	# reattach dependents to the switch
	###################################		
	deSel()
	dummy['selected'].setValue(True)
	dummy.setInput(0, switch)
	nukescripts.node_delete()
	
	deSel()
	
	return
	
########################
	
def dollAlignNodes():
	##################################################################
	# figure out which axis the nodes are most likely to be aligned to
	##################################################################
	if len(nuke.selectedNodes()) < 2:
		nuke.message("Please selected at least two nodes.")
		return
	xPos = []
	yPos = []
	xSum = 0
	ySum = 0
	xDev = []
	yDev = []
	xDevSum = 0
	yDevSum = 0
	for node in nuke.selectedNodes():
		xPos.append(node['xpos'].value())
		yPos.append(node['ypos'].value())
	for i in xPos:
		xSum += i
	for i in yPos:
		ySum += i
	xAvg = xSum / len(xPos)
	yAvg = ySum / len(yPos)
	for i in xPos:
		xDev.append(i - xAvg)
	for i in yPos:
		yDev.append(i - yAvg)
	for i in xDev:
		xDevSum += abs(i)
	for i in yDev:
		yDevSum += abs(i)
	xDevAvg = xDevSum / len(xDev)
	yDevAvg = yDevSum / len(yDev)	
	
	#####################################
	# ask user for which axis to align to
	#####################################
	if xDevAvg > yDevAvg:
		bestGuess = "x y"
	else:
		bestGuess = "y x"
	p = nuke.Panel("Align to which axis?")
	alignChoice = "Align to Axis: "
	p.addEnumerationPulldown(alignChoice, bestGuess)
	success = p.show()
	if not success:
		return

	############################		
	# align nodes to chosen axis
	############################
	chosen = p.value(alignChoice)
	if chosen == "x":
		for node in nuke.selectedNodes():
			node['ypos'].setValue(yAvg)
	else:
		for node in nuke.selectedNodes():
			node['xpos'].setValue(xAvg)

	return

###########################
###########################
##         END OF        ##
## DOLL CUSTOM FUNCTIONS ##
###########################
###########################


	

# Create a dictionary of aliases and the node class they reference to
nodeAliases = {
        "Lookup" : "ColorLookup",
        "Spline" : "Bezier",
        "Grad" : "Ramp",
	"Keep" : "Remove",
	"Lumakey" : "Keyer",
	"Channels" : "Shuffle"

}

# Build all menu entries for your aliased nodes
n = nuke.menu("Nodes").addMenu("Other/Aliased nodes")
for a,i in nodeAliases.items():
  s = a.upper()
  p = n.addMenu(s[0])
  p.addCommand(a, "nuke.createNode('"+i+"')") 
  
n.addCommand('Open Comp_Controls', "nuke.show(nuke.toNode('COMP_CONTROLS'))", 'Alt+v')
n.addCommand('Create Precomp setup', "dollPcompCreate()", 'Alt+p')
n.addCommand('Align to axis', "dollAlignNodes()", 'Alt+l')

