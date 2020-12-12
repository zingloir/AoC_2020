import re


def calc_pos(instruction, position, direction):
    directions = ['N', 'S', 'W', 'E']
    if instruction[0] in directions:
        return calc_diff(instruction[0], int(instruction[1]), position), direction
    if instruction[0] == 'F':
        return calc_diff(direction, int(instruction[1]), position), direction
    else:
        return position, calc_dir(direction, instruction[0], int(instruction[1]))


def calc_diff(dir, dis, pos):
    if dir == 'N':
        return [pos[0] + dis, pos[1]]
    if dir == 'S':
        return [pos[0] - dis, pos[1]]
    if dir == 'E':
        return [pos[0], pos[1] + dis]
    if dir == 'W':
        return [pos[0], pos[1] - dis]


def calc_dir(dir_old, turn_dir, deg):
    directions = ['E', 'S', 'W', 'N']
    deg = deg // 90
    j = 0
    while j < len(directions):
        if directions[j] == dir_old:
            break
        j += 1
    if turn_dir == 'L':
        return directions[j - deg]
    if turn_dir == 'R':
        return directions[(j + deg) % 4]


with open("input") as f:
    lines = f.read().split('\n')

instr = []
for i in range(len(lines)):
    match = re.match('([A-Z])([0-9]+)', lines[i])
    instr.append(list(match.group(i) for i in range(1, 3)))

# 0 East, 1 South, 2 West, 3 North
cur_pos = [0, 0]
cur_dir = 'E'
for inst in instr:
    cur_pos, cur_dir = calc_pos(inst, cur_pos, cur_dir)

print(abs(cur_pos[0]) + abs(cur_pos[1]))
