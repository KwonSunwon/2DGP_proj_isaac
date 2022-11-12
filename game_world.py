
# layer 0: background(stage)
# layer 1: objects(room objects, item)
# layer 2: creature(player, enemy)
# layer 3: flying creature(enemy)
# layer 4: effects
# layer 5: ui

objects = [[], [], [], [], [], []]
collision_group = dict()

def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += l


def remove_object(o):
    for i in objects:
        if o in i:
            i.remove(o)
            remove_collision_group(o)
            del o
            break


def clear():
    for o in all_objects():
        del o
    for l in objects:
        l.clear()


def destroy():
    clear()
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o


def add_collision_group(a, b, group):
    if group not in collision_group:
        collision_group[group] = [[],[]]

    if a:
        if type(a) == list:
            collision_group[group][0] += a
        else:
            collision_group[group][0].append(a)
            
    if b:
        if type(b) == list:
            collision_group[group][1] += b
        else:
            collision_group[group][1].append(b)
            

def all_collision_pairs():
    for group, pairs in collision_group.items():
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group


def remove_collision_group(o):
    for pairs in collision_group.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        elif o in pairs[1]:
            pairs[1].remove(o)
            
            