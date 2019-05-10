def vectorDistance():
	nodelist = nuke.selectedNodes()
	if len(nodelist) != 2:
		print "Error!"
		return
	try:
		pos1 = nodelist[0]['translate'].value()
		pos2 = nodelist[1]['translate'].value()
		dist = math.sqrt( pow(pos1[0]-pos2[0],2) + pow(pos1[1]-pos2[1],2) + pow(pos1[2]-pos2[2],2) )
		print dist
		dispMssg = "Distance is: " + str(dist)
		nuke.message(dispMssg)
		return
	except:
		nuke.message("Some error occurred. Try selecting two node with 3D positions")
		pass
