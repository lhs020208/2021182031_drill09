# world [0] : background
# world [1] : foreground
# world [2] : 이찌방 foreground
world = [[],[],[]]

def add_object(o,depth):
    world[depth].append(o)

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    print(f'critical: 없는거{o} 지우려 함!')