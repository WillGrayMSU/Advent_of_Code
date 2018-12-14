
def readInput(filename):
    lines =0
    columns = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
    with open(filename, 'r') as f:
        columns = len(f.readline())-1

    world = []
    for each in range(columns):
        world.append([])

    f = open(filename, 'r')

    for i in range(lines):
        for j in range(columns):
            char = f.read(1)
            if char != "\n":
                world[i].append(char)

    return world

