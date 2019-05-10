def alignNodes():
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
