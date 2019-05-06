import nuke
import math
import time,re,subprocess

###########################
###########################
##                       ##
## DOLL CUSTOM FUNCTIONS ##
##                       ##
###########################
###########################


def rvFinalCheck(nodelist):
    cmd = ['/Applications/RV64.app/Contents/MacOS/RV64']
    for node in nodelist:
        cmd.append(node['file'].value())
    cmd.append('-over')
    ocmd = ' '.join(cmd)
    subprocess.Popen(ocmd, shell=True)


def vectorDistance():
	nodelist = nuke.selectedNodes()
	if len(nodelist) != 2:
		print "Error!"
		return
	
	try:
		pos1 = nodelist[0]['translate'].value()
		pos2 = nodelist[1]['translate'].value()
		dist = math.sqrt(pow(pos1[0]-pos2[0],2) + pow(pos1[1]-pos2[1],2) + pow(pos1[2]-pos2[2],2) )
		print dist
		dispMssg = "Distance is: " + str(dist)
		nuke.message(dispMssg)
		return
		
	except:
		nuke.message("Encoutered a problem. \nProbably you have not selected 2 and only 2 nodes with a 3D position")
		pass

#########################

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

def publishThisShot(n):
	origfileset = n['file'].value()
	filesetname = os.path.basename(origfileset).split('.')[0]
	pubfileset  = re.sub(r'img/rndr/comp',r'publish/comp',origfileset)
	herofileset = re.sub(r'\Dv\d+','',pubfileset)
	pubdir  = os.path.dirname(pubfileset)
	herodir = os.path.dirname(herofileset)

	if not os.path.isdir(pubdir):
		os.mkdir(pubdir)

	if not os.path.isdir(herodir):
		os.mkdir(herodir)



	nukefiledir  = os.path.join('/'.join(origfileset.split('/')[:8]),'nuke','nk')
	nukefilename = os.path.join(nukefiledir,filesetname) + '.nk'
	nukepubname  = re.sub(r'/nuke/nk/',r'/publish/nk/',nukefilename)

	if not os.path.isfile(nukefilename):
		nuke.message("Publish failed to find a nuke file to match your comp fileset.\nFunctionality to choose a different nk file not yet implemented.")
		return

	#copy the nuke file to publish directory
	nkcmd = 'cp ' + re.sub(r' ', '\ ',nukefilename) + ' ' + re.sub(r' ', '\ ',nukepubname)
	print nkcmd
	subprocess.Popen(nkcmd,shell=True)

	#if file is a quicktime, then copy the QT and quit
	if os.path.splitext(origfileset)[1] == '.mov':
		movcmd = 'cp ' + re.sub(r' ', '\ ',origfileset) + ' ' + re.sub(r' ', '\ ',pubfileset)
		subprocess.Popen(movcmd,shell=True)
		print "copied the quicktime to publish directory"
		return


	#remove all files in the hero fileset
	rmcmd = 'rm ' + herodir + '/* -rf'
	subprocess.Popen(rmcmd,shell=True)

	#copy the frames and symlink the hero fileset
	first = n.frameRange().first()
	last  = n.frameRange().last()
	i = first

	taskProg = 0.0
	numTasks = last - first
	taskIncr = (1.0/numTasks)*100
	task = nuke.ProgressTask("Publishing shot")

	while i <= last:
		tmssg = 'Doing frame' + str(i)
		task.setMessage(tmssg)
		task.setProgress(int(taskProg))
		curFile = re.sub(r'%d',str(i),origfileset)
		curPub  = re.sub(r'%d',str(i),pubfileset)
		curHero = re.sub(r'%d',str(i),herofileset)
		tempHero = os.path.join(herodir, os.path.basename(curPub))


	    #copy files
		copyFiles = 'cp ' + re.sub(r' ', '\ ',curFile) + ' ' + re.sub(r' ', '\ ',curPub)
		#symlink from versioned publish to non-versioned hero
		symLink = 'ln -s ' + re.sub(r' ', '\ ',curPub) + ' ' + re.sub(r' ', '\ ',herodir) + '/'
		#rename symlink file to have no version
		renameFiles = 'mv ' + re.sub(r' ', '\ ',tempHero) + ' ' + re.sub(r' ', '\ ',curHero)

		subprocess.Popen(copyFiles,shell=True)
		subprocess.Popen(symLink,shell=True)
		time.sleep(2)
		subprocess.Popen(renameFiles,shell=True)


		taskProg = taskProg + taskIncr
		i +=1
	del(task)
	return

###########################
###########################
##         END OF        ##
## DOLL CUSTOM FUNCTIONS ##
###########################
###########################