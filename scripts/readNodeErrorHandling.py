for node in nuke.selectedNodes():
	if node.Class() != "Read":
		continue
	node['on_error'].setValue('nearest frame')
	#node['disable'].setExpression('hasError')
