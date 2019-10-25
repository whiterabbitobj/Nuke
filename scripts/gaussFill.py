def gaussFillCallback():
	n = nuke.thisNode()
	k = nuke.thisKnob()

	if k.name() == "fillAmt":
		adjust_levels(n, k)

	return

def adjust_levels(node, knob):
	node.begin()
	i = nuke.toNode("Input1")
	o = nuke.toNode("Output1")
	
	delete_existing(i, o)

	connect_me = create_fill(i, 1)

	for x in range(1, int(knob.value())):
		connect_me = create_fill(connect_me, x+1)

	o.setInput(0, connect_me)

def delete_existing(i, o):
	for node in nuke.allNodes():
		if node in [i,o]:
			print "node {} is protected!".format(node.name().upper())
			continue
		nuke.delete(node)

def create_fill(top, amt):
	print "creating level: {}".format(amt)
	x = top.xpos()
	y = 0

	nodes = [nuke.createNode("Blur", "size {} mix parent.gaussMix".format(amt), inpanel=False),
			nuke.createNode("Unpremult", inpanel=False),
			nuke.createNode("ChannelMerge", "operation divide", inpanel=False),
			nuke.createNode("FilterErode", "filter gaussian", inpanel=False),
			nuke.createNode("Grade", "channels alpha gamma parent.gammaFix", inpanel=False),
			nuke.createNode("Premult", inpanel=False)]

	for i, node in enumerate(nodes):
		node.setInput(0, top)
		node.setXYpos(x+150, y)
		if node.Class() == "FilterErode" or node.Class() == "Blur":
			node['size'].setExpression('parent.blurScalar * {}'.format(amt+1))
		top = node
		y += 50
	#top.setInput(1, nodes[0])
	return top
