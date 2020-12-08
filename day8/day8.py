import re
with open('input') as f:
    lines = f.readlines()

# Arbeitet input von Anfang bis Ende durch, gibt Wert des Accumulators zurück
def startup():
    visited = []
    pos = 0
    accu = 0
    while pos in range(len(tasks)):
        visited.append(pos)
        if tasks[pos][0] == 'acc':
            accu += int(tasks[pos][1])
            pos += 1
        elif tasks[pos][0] == 'nop':
            pos += 1
        elif tasks[pos][0] == 'jmp':
            pos += int(tasks[pos][1])
        if pos in visited:
            break
    return accu

# Prüft, ob input mit reparierter Stelle erfolgreich durchläuft
def try_me():
    visited = []
    pos = 0
    accu = 0
    while pos < len(repair):
        visited.append(pos)
        if repair[pos][0] == 'jmp':
            pos += int(repair[pos][1])
        else:
            pos += 1
        if pos in visited:
            break
    if pos == len(repair):
        return True
    else:
        return False

# Input bereinigen
tasks = []
for line in lines:
    match = re.match('([a-z]+) ([+|-]\d+)', line)
    match = [match.group(1), match.group(2)]
    tasks.append(match)

# Part 1
print('Accumulator an erster doppelter Position: ' + str(startup()))

# Part 2
repair = tasks
for i in range(len(tasks)):
    if tasks[i][0] == 'jmp':
        repair[i][0] = 'nop'
        if try_me():
            tasks = repair
            break
        else:
            repair[i][0] = 'jmp'
print('Accumulator nach Reparatur: ' + str(startup()))