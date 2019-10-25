

import os.path as path
for read in nuke.allNodes("Read"):
    f = nuke.filename(read)
    dir = path.dirname(f)
    fname = path.basename(f).split('.')[0]
    
    for curFile in nuke.getFileNameList(dir):
        if curFile.startswith(fname):
            newFile = path.join(dir, curFile)
            print "updating {} to: {}".format(read.name(), newFile)
            read['file'].fromUserText(newFile)
            break
