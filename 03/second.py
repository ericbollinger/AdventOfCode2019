import sys, os
sys.path.append(os.path.relpath("../lib"))
from reader import read_lists
from string import upper

def calc_coords(src, mvmt):
    direction = mvmt[0]
    length = int(mvmt[1:])

    result = list(src)

    result[2] += length

    if direction == 'R':
        result[0] += int(length)
    elif direction == 'L':
        result[0] -= int(length)
    elif direction == 'U':
        result[1] += int(length)
    else:
        result[1] -= int(length)

    print(result[2])
    return result

def get_collision(line1, line2):
    l1p1 = line1[0]
    l1p2 = line1[1]
    l2p1 = line2[0]
    l2p2 = line2[1]

    if (l1p1[0] == l1p2[0] and l2p1[1] == l2p2[1]):
        # l1 is vertical, l2 is horizontal
        hix = max(l2p1[0], l2p2[0])
        lox = min(l2p1[0], l2p2[0])
        hiy = max(l1p1[1], l1p2[1])
        loy = min(l1p1[1], l1p2[1])

        if (lox < l1p1[0] < hix):
            if (loy < l2p1[1] < hiy):
                l1d = l1p2[2] - (abs(l1p2[1] - l2p1[1]))
                print("l1d: {} - ({} - {}) = {}".format(l1p2[2], abs(l1p2[1]), abs(l2p1[1]), l1d))
                l2d = l2p2[2] - (abs(l2p2[0]) - abs(l1p1[0]))
                print("l2d: {} - ({} - {}) = {}".format(l2p2[2], abs(l2p2[0]), abs(l1p1[0]), l2d))
                return [l1p1[0], l2p1[1], l1d, l2d]

    elif (l1p1[1] == l1p2[1] and l2p1[0] == l2p2[0]):
        # l1 is horizontal, l2 is vertical
        hix = max(l1p1[0], l1p2[0])
        lox = min(l1p1[0], l1p2[0])
        hiy = max(l2p1[1], l2p2[1])
        loy = min(l2p1[1], l2p2[1])

        if (lox < l2p1[0] < hix):
            if (loy < l1p1[1] < hiy):
                l1d = l1p2[2] - (abs(l1p2[0] - l2p1[0]))
                print("l1d: {} - ({} - {}) = {}".format(l1p2[2], abs(l1p2[0]), abs(l2p1[0]), l1d))
                l2d = l2p2[2] - (abs(l2p2[1] - l1p1[1]))
                print("l2d: {} - ({} - {}) = {}".format(l2p2[2], abs(l2p2[1]), abs(l1p1[1]), l2d))
                return [l2p1[0], l1p1[1], l1d, l2d]

    return None

#wires_input = read_lists("in.txt", ",")
#wires_input = read_lists("in2.txt", ",")
wires_input = read_lists("input.txt", ",")

paths = []
paths.append([[0,0,0]])
paths.append([[0,0,0]])

for i,wire in enumerate(wires_input):
    for j,pair in enumerate(wire):
        last_coord = paths[i][len(paths[i])-1]
        paths[i].append(calc_coords(last_coord, pair))


intersections = []

for i in range(0, len(paths[0])-1):
    for j in range(0, len(paths[1])-1):
        line1 = [paths[0][i], paths[0][i+1]]
        line2 = [paths[1][j], paths[1][j+1]]
        collision = get_collision(line1, line2)
        if (collision):
            print("Collision found: {}".format(collision))
            intersections.append(collision)

lowest = 999999
for i in intersections:
    lowest = min(lowest, i[2] + i[3])
print("Lowest: {}".format(lowest))
