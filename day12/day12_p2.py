import re


def calc_pos(instruction, shippos, wppos):
    directions = ['N', 'S', 'W', 'E']
    if instruction[0] in directions:
        return shippos, calc_diff(instruction[0], int(instruction[1]), wppos)
    if instruction[0] == 'F':
        return move_ship(shippos, wppos, int(instruction[1])), wppos
    else:
        return shippos, calc_dir(wppos, instruction[0], int(instruction[1]))


def calc_diff(dir, dis, pos):
    if dir == 'N':
        return [pos[0] + dis, pos[1]]
    if dir == 'S':
        return [pos[0] - dis, pos[1]]
    if dir == 'E':
        return [pos[0], pos[1] + dis]
    if dir == 'W':
        return [pos[0], pos[1] - dis]


def calc_dir(wppos, turn_dir, deg):
    directions = ['E', 'S', 'W', 'N']
    if wppos[0] < 0:
        ydir = 'S'
    else:
        ydir = 'N'

    if wppos[1] < 0:
        xdir = 'W'
    else:
        xdir = 'E'

    deg = deg // 90
    wptemp = [ydir, abs(wppos[0]), xdir, abs(wppos[1])]

    x = 0
    y = 0
    while x < len(directions):
        if directions[x] == xdir:
            break
        x += 1

    y = 0
    while y < len(directions):
        if directions[y] == ydir:
            break
        y += 1

    if turn_dir == 'L':
        wptemp[0] = directions[y - deg]
        wptemp[2] = directions[x - deg]
    if turn_dir == 'R':
        wptemp[0] = directions[(y + deg) % 4]
        wptemp[2] = directions[(x + deg) % 4]

    j = 0
    xdirs = ['W', 'E']

    if wptemp[0] in xdirs:
        if wptemp[0] == 'W':
            newxpos = 0 - wptemp[1]
        else :
            newxpos = wptemp[1]
        if wptemp[2] == 'S':
            newypos = 0 - wptemp[3]
        else:
            newypos = wptemp[3]
    else:
        if wptemp[2] == 'W':
            newxpos = 0 - wptemp[3]
        else:
            newxpos = wptemp[3]
        if wptemp[0] == 'S':
            newypos = 0 - wptemp[1]
        else:
            newypos = wptemp[1]

    return [newypos, newxpos]


def move_ship(shippos, wppos, count):
    return [shippos[0] + wppos[0] * count, shippos[1] + wppos[1] * count]


with open("input") as f:
    lines = f.read().split('\n')

instr = []
for i in range(len(lines)):
    match = re.match('([A-Z])([0-9]+)', lines[i])
    instr.append(list(match.group(i) for i in range(1, 3)))

# 0 East, 1 South, 2 West, 3 North
ship_pos = [0, 0]
wp_pos = [1, 10]
for inst in instr:
    ship_pos, wp_pos = calc_pos(inst, ship_pos, wp_pos)

print(abs(ship_pos[0]) + abs(ship_pos[1]))
