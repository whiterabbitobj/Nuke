import random

def makerCallback():
	# VARS
	NEEDLENAME = 'needles'
	BOUGHNAME = 'boughs'
	WREATHNAME = 'wreath'

	parent = nuke.thisNode()
	knob = nuke.thisKnob()
	kname = knob.name()
	parent.begin()

	if kname == 'randSeed':
		setExpressions(getNodes(NEEDLENAME), knob.value(), NEEDLENAME)
		setExpressions(getNodes(BOUGHNAME), knob.value(), BOUGHNAME)

	if kname == 'needlesNum':
		wMaker(parent, knob, NEEDLENAME)

	if kname == 'boughsNum':
		wMaker(parent, knob, BOUGHNAME)

	if kname == 'wreathNum':
		makeWreath(parent, knob, WREATHNAME)

	return



def touchMergeGeo(merge_name, xpos, ypos):
	merge = nuke.toNode(merge_name)
	if merge is None:	
		merge = nuke.createNode("MergeGeo", 'name {}'.format(merge_name))
	merge.setXYpos(xpos+100, ypos-50)
	disconnectNode(merge)
	return merge

def touchOffsetGeo(offset_name, xpos, ypos):
	offset = nuke.toNode(offset_name)
	if offset is None:	
		offset = nuke.createNode("TransformGeo", 'name {}'.format(offset_name))
	offset.setXYpos(xpos+100, ypos+50)
	disconnectNode(offset)
	return offset



def makeWreath(parent, knob, item_name):
	'''
	Repeats a number of boughs to create a wreath.
	'''
	dot_in = nuke.toNode("{}_in".format(item_name))
	dot_out = nuke.toNode("{}_out".format(item_name))
	max_items = int(knob.value())
	rot_interval = 360 / max_items

	seed = parent['randSeed'].value()

	### TransformGeo node
	offset = touchOffsetGeo('offset{}'.format(item_name), dot_in.xpos(),dot_in.ypos())
	offset['translate'].setExpression('parent.wreathScale', 1)
	#offset['pivot'].setExpression('-parent.wreathScale', 1)
	offset['rotate'].setExpression('parent.wreathRotBounds',0)
	offset.setInput(0, dot_in)
	noSelect()

	### MergeGeo node
	merge = touchMergeGeo('{}Merge'.format(item_name), dot_in.xpos(),dot_out.ypos())
	noSelect()

	### Grab existing items
	cur_items = getNodes(item_name)

	### Delete items if more exist than requested
	while len(cur_items) > max_items:
		nuke.delete(cur_items.pop())

	### Create items if not enough exist
	for i in range(len(cur_items), max_items):
		t = nuke.createNode("TransformGeo", 'name {}{}'.format(item_name, i+1), inpanel=False)
		cur_items.append(t)

	### Set inputs of transforms and merge
	for i, t in enumerate(cur_items):
		t['rotate'].setValue(rot_interval * i, 0)
		t.setXYpos(100 * i + merge.xpos(), dot_in.ypos()+100)
		t.setInput(0, offset)
		merge.setInput(i, t)

	### Set the dot signifying the end of the region to pipe into the MergeGeo
	dot_out.setInput(0, merge)

	#### De-select all nodes
	noSelect()
	return



def wMaker(parent, knob, item_name):
	'''
	Creates or destroys extra items based on user-input and	set random values 
	to the translational params.
	'''
	dot_in = nuke.toNode("{}_in".format(item_name))
	dot_out = nuke.toNode("{}_out".format(item_name))
	max_items = int(knob.value())
	seed = parent['randSeed'].value()

	### Check if the MergeGeo is created, if not, create it, 
	### otherwise, move on
	merge = touchMergeGeo('{}Merge'.format(item_name), dot_in.xpos(),dot_out.ypos())

	#### De-select all nodes
	noSelect()

	### Grab existing items
	cur_items = getNodes(item_name)

	### Delete items if more exist than requested
	while len(cur_items) > max_items:
		nuke.delete(cur_items.pop())

	### Create items if not enough exist
	for i in range(len(cur_items), max_items):
		t = nuke.createNode("TransformGeo", 'name {}{}'.format(item_name, i+1), inpanel=False)
		cur_items.append(t)

	### Set random expressions
	setExpressions(cur_items, seed, item_name)

	### Set inputs of transforms and merge
	for i, t in enumerate(cur_items):
		t.setXYpos(100 * i + merge.xpos(), dot_in.ypos()+100)
		t.setInput(0, dot_in)
		merge.setInput(i, t)

	### Set the dot signifying the end of the region to pipe into the MergeGeo
	dot_out.setInput(0, merge)

	#### De-select all nodes
	noSelect()
	return



def setExpressions(items, seed, param_name):
	'''
	Adds repeatably random expressions to knobs.
	'''
	for i, node in enumerate(items):
		random.seed(seed * i)
		genRandomExpression(node['translate'], ' * parent.{0}TransRandomness * parent.{0}TransBounds'.format(param_name))
		genRandomExpression(node['rotate'], ' * parent.{0}RotRandomness * parent.{0}RotBounds'.format(param_name), bounded=False)
		genRandomExpression(node['scaling'], ' * parent.{0}ScaleRandomness * parent.{0}ScaleBounds + 1'.format(param_name), curved=False)

	

def genRandomExpression(knob, expression, bounded=True, curved=True):
	for i in range(3):
		rand = random.uniform(-1 * (1-bounded),1)
		rand_expr = '{} {}'.format(rand, expression)
		knob.setExpression(rand_expr, channel = i)
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
