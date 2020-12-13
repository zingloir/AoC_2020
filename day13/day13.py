# Input bereinigen. Schreibt eigene früheste Abfahrtzeit in depart
# und alle vorhandenen Buslinien in busses, ohne x dazwischen
with open('input') as f:
    lines = f.read().split('\n')
    depart = int(lines.pop(0))
    lines = lines[0].split(',')
    busses = []
    offsets = {}
    for i in range(len(lines)):
        if lines[i] != 'x':
            offsets[int(lines[i])] = i
            busses.append(int(lines[i]))

# Part 1
nextdepart = []
for bus in busses:
    nextdepart.append(bus * ((depart // bus) + 1))

print((min(nextdepart) - depart) * busses[nextdepart.index(min(nextdepart))])


found = False
i = 0
while not found:
    i += 1
    found = True
    for bus in busses:
        if ((max(busses) * i) - offsets[max(busses)] + offsets[bus]) % bus == 0:
            continue
        else:
            found = False
            break

print((i * max(busses)) - offsets[max(busses)] + offsets[busses[-1]])
