import nuke

def make_backdrop(nodes):
    x = min([node.xpos() for node in nodes])
    y = min([node.ypos() for node in nodes])
    width = max([node.xpos() + node.screenWidth() for node in nodes]) - x
    height = max([node.ypos() + node.screenHeight() for node in nodes]) - y
    l, r, t, b = (-60, 60, -180, 60)

    bd = nuke.createNode("BackdropNode")
    bd.setXYpos(x + l, y + t)
    bd['bdwidth'].setValue(width + r - l)
    bd['bdheight'].setValue(height + b - t)
    bd['tile_color'].setValue(640034559)
    bd['note_font_color'].setValue(1886417151)
    bd['note_font_size'].setValue(125)
    bd['note_font'].setValue("Verdana Bold")
    # add z_order functionality later, see the Foundry backdrop scripts
    # for further info
