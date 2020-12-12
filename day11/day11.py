with open('input') as f:
    lines = f.read().split('\n')

def splitit(line):
    return [char for char in line]

def occu_count(grid):
    occu_counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                occu_counter += 1
    return occu_counter


grid = [[]] * len(lines)
for i in range(len(lines)):
    grid[i] = splitit(lines[i])

grid2 = [[]] * len(lines)
for i in range(len(lines)):
    grid2[i] = splitit(lines[i])

occup = []
for i in range(len(grid)):
    occup.append([0] * len(grid[i]))

occup2 = []
for i in range(len(grid)):
    occup2.append([0] * len(grid[i]))

change = True
while change:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            occup[i][j] = 0
            if grid[i][j] == '#' or grid[i][j] == 'L':
                for k in range(-1, 2):
                    if j + k < 0:
                        continue
                    if j + k >= len(grid[i]):
                        continue
                    if i - 1 >= 0:
                        if grid[i - 1][j + k] == '#':
                            occup[i][j] += 1
                    if i + 1 < len(grid):
                        if grid[i + 1][j + k] == '#':
                            occup[i][j] += 1
            if j < len(grid[i]) - 1:
                if grid[i][j + 1] == '#':
                    occup[i][j] += 1
            if j > 0:
                if grid[i][j - 1] == '#':
                    occup[i][j] += 1

    change = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                if occup[i][j] >= 4:
                    grid[i][j] = grid[i][j].replace('#', 'L')
                    change = True
            if grid[i][j] == 'L':
                if occup[i][j] == 0:
                    grid[i][j] = grid[i][j].replace('L', '#')
                    change = True

print("Part 1: " + str(occu_count(grid)))

# Part 2 _______________________________________________________________
change = True
while change:
    for i in range(len(grid2)):
        for j in range(len(grid2[i])):
            occup2[i][j] = 0
            # Left
            l = 1
            while j - l >= 0:
                if grid2[i][j - l] == 'L':
                    break
                elif grid2[i][j - l] == '#':
                    occup2[i][j] += 1
                    break
                l += 1
            # Right
            r = 1
            while j + r < len(grid2[i]):
                if grid2[i][j + r] == 'L':
                    break
                elif grid2[i][j + r] == '#':
                    occup2[i][j] += 1
                    break
                r += 1
            # Up
            u = 1
            while i - u >= 0:
                if grid2[i - u][j] == 'L':
                    break
                elif grid2[i - u][j] == '#':
                    occup2[i][j] += 1
                    break
                u += 1
            # Down
            d = 1
            while i + d < len(grid2):
                if grid2[i + d][j] == 'L':
                    break
                elif grid2[i + d][j] == '#':
                    occup2[i][j] += 1
                    break
                d += 1
            # Up Left
            ul = 1
            while i - ul >= 0 and j - ul >= 0:
                if grid2[i - ul][j - ul] == 'L':
                    break
                elif grid2[i - ul][j - ul] == '#':
                    occup2[i][j] += 1
                    break
                ul += 1
            # Up Right
            ur = 1
            while i - ur >= 0 and j + ur < len(grid2[i]):
                if grid2[i - ur][j + ur] == 'L':
                    break
                elif grid2[i - ur][j + ur] == '#':
                    occup2[i][j] += 1
                    break
                ur += 1
            # Down Left
            dl = 1
            while i + dl < len(grid2) and j - dl >= 0:
                if grid2[i + dl][j - dl] == 'L':
                    break
                elif grid2[i + dl][j - dl] == '#':
                    occup2[i][j] += 1
                    break
                dl += 1
            # Down Right
            dr = 1
            while i + dr < len(grid2) and j + dr < len(grid2[i]):
                if grid2[i + dr][j + dr] == 'L':
                    break
                elif grid2[i + dr][j + dr] == '#':
                    occup2[i][j] += 1
                    break
                dr += 1

    change = False
    for i in range(len(grid2)):
        for j in range(len(grid2[i])):
            if grid2[i][j] == '#':
                if occup2[i][j] >= 5:
                    grid2[i][j] = grid2[i][j].replace('#', 'L')
                    change = True
            if grid2[i][j] == 'L':
                if occup2[i][j] == 0:
                    grid2[i][j] = grid2[i][j].replace('L', '#')
                    change = True

print("Part 2: " + str(occu_count(grid2)))
