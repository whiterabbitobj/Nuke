def refreshAllReads():
    for node in nuke.allNodes("Read"):
    	node['reload'].execute()
	
def rar():
	refreshAllReads()

def refreshreads():
	refreshAllReads()
	
def refreshallreads():
	refreshAllReads()	