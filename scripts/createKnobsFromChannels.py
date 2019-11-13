n = nuke.toNode('Group1')
maxLen = max([len(chan.split('.')[-1]) for chan in n.channels()])

n.begin()
nuke.toNode('Input1')['selected'].setValue(True)

for chan in n.channels():
    name = chan.split('.')[-1]
    boolName = "do" + name
    sliderName = "mix"+name
    b = nuke.Boolean_Knob(boolName, name.ljust(maxLen))
    s = nuke.Double_Knob(sliderName, '', )
    b.setFlag(nuke.STARTLINE)
    s.clearFlag(nuke.STARTLINE)
    n.addKnob(b)
    n.addKnob(s)
    g = nuke.createNode("Grade",inpanel=False)
    g['channels'].setValue(chan)
    g['multiply'].setExpression("parent.{}".format(sliderName))
    g['white'].setExpression("parent.{}".format(boolName))
nuke.toNode("Output1").setInput(0, g)
n.end()
