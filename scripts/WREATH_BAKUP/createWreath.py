import random

def makerCallback():
	# VARS
	NEEDLENAME = 'needle'
	BOUGHNAME = 'bough'

	parent = nuke.thisNode()
	knob = nuke.thisKnob()
	kname = knob.name()
	parent.begin()

	if kname == 'needlesNum':
		makeTuft(parent, knob, NEEDLENAME)
	if kname == 'randSeed':
		setNeedleExpressions(getNodes(NEEDLENAME), knob.value())
	if kname == 'boughsNum':
		makeBough(parent, knob, BOUGHNAME)
	if kname == 'wreathNum':
		makeWreath()

	return




def touchMergeGeo(mergeName, xpos, ypos):
	merge = nuke.toNode(mergeName)
	if merge is None:	
		merge = nuke.createNode("MergeGeo", 'name {}'.format(mergeName))
	merge.setXYpos(xpos+100, ypos-50)
	disconnectNode(merge)
	return merge



def makeWreath():
	return



def makeTuft(parent, knob, NEEDLENAME):
	tuft_in = nuke.toNode("tuft_in")
	tuft_out = nuke.toNode("tuft_out")

	### Check if the MergeGeo is created, if not, create it, 
	### otherwise, move on
	merge = touchMergeGeo('tuftMerge', tuft_in.xpos(),tuft_out.ypos())

	#### De-select all nodes
	noSelect()

	### Grab existing needles
	curNeedles = getNodes(NEEDLENAME)

	### Delete Needles if more exist than requested
	maxNeedles = int(parent['needlesNum'].value()) 
	while len(curNeedles) > maxNeedles:
		nuke.delete(curNeedles.pop())

	### Create Needles if not enough exist
	for i in range(len(curNeedles), maxNeedles):
		t = nuke.createNode("TransformGeo", 'name {}{}'.format(NEEDLENAME, i+1), inpanel=False)
		curNeedles.append(t)

	### Set Needle expressions
	setNeedleExpressions(curNeedles, parent['randSeed'].value())

	### Set inputs of transforms and merge
	for i, t in enumerate(curNeedles):
		t.setXYpos(100 * i + merge.xpos(), tuft_in.ypos()+50)
		t.setInput(0, tuft_in)
		merge.setInput(i, t)

	### Set the dot signifying the end of the Tuft region to pipe into the MergeGeo
	tuft_out.setInput(0, merge)

	#### De-select all nodes
	noSelect()
	return



def makeBough(parent, knob, basename):
	dot_in = nuke.toNode("boughs_in")
	dot_out = nuke.toNode("boughs_out")

	### Check if the MergeGeo is created, if not, create it, 
	### otherwise, move on
	merge = touchMergeGeo('boughsMerge', dot_in.xpos(), dot_out.ypos())

	#### De-select all nodes
	noSelect()

	### Grab existing boughs
	curItems = getNodes(basename)

	### Delete Boughs if more exist than requested
	maxItems = int(parent['boughsNum'].value()) 
	while len(curItems) > maxItems:
		nuke.delete(curItems.pop())

	### Create Boughs if not enough exist
	for i in range(len(curItems), maxItems):
		t = nuke.createNode("TransformGeo", 'name {}{}'.format(basename, i+1), inpanel=False)
		curItems.append(t)

	### Set Needle expressions
	setBoughExpressions(curItems, parent['randSeed'].value())

	### Set inputs of transforms and merge
	for i, t in enumerate(curItems):
		t.setXYpos(100 * i + merge.xpos(), dot_in.ypos()+50)
		t.setInput(0, dot_in)
		merge.setInput(i, t)

	### Set the dot signifying the end of the Tuft region to pipe into the MergeGeo
	dot_out.setInput(0, merge)
	return



def setNeedleExpressions(needles, seed):
	for i, node in enumerate(needles):
		random.seed(seed * i)
		genRandomExpression(node['rotate'], ' * parent.needlesRotRandomness * parent.needlesRotBounds')
		genRandomExpression(node['translate'], ' * parent.needlesTransRandomness * parent.needlesTransBounds')
		genRandomExpression(node['scaling'], ' * parent.needlesScaleRandomness * parent.needlesScaleBounds + 1', bounded=True)



def setBoughExpressions(needles, seed):
	for i, node in enumerate(needles):
		random.seed(seed * i * -2)
		#genRandomExpression(node['rotate'], ' * parent.boughsRotRandomness * parent.boughsRotBounds')
		genRandomExpression(node['translate'], ' * parent.boughsTransRandomness * parent.boughsTransBounds')
		#genRandomExpression(node['scaling'], ' * parent.boughsScaleRandomness * parent.boughsScaleBounds + 1', bounded=True)


	
def genRandomExpression(knob, expression, bounded=False):
	for i in range(3):
		randRot = random.uniform(-1 * (1-bounded),1)
		rotExpr = '{} {}'.format(randRot, expression)
		knob.setExpression(rotExpr, channel = i)
	return



def disconnectNode(node):
	for i in range(node.inputs()):
		node.setInput(i, None)
	return



def getNodes(basename):
	return sorted([node for node in nuke.allNodes("TransformGeo") if 
			node.name().startswith(basename)], key=lambda x: x.name())



def noSelect():
	for node in nuke.selectedNodes():
		node['selected'].setValue(False)
	return
