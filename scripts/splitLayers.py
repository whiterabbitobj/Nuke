def splayLayers(n):
	x = n.xpos()
	y = n.ypos() + 100
	layers = list( set( [c.split('.')[0] for c in n.channels()] ) )

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
