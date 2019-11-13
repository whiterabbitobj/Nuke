### set node color to light green
for node in nuke.selectedNodes():
    node['tile_color'].setValue(1975810815)

### fix read node stuff
for node in nuke.selectedNodes("Read"):
    node['before'].setValue("black")
    node['after'].setValue("black")
    node['label'].setValue("[value first] - [value last]")

### print enabled write nodes
for node in nuke.allNodes("Write"):
    if not node['disable'].value():
        print node.name()
