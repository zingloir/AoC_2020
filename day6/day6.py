with open ('input') as f:
    lines = f.read().split('\n\n')
print(lines)

# Fügt jeden Buchstaben, der im Input vorkommt, genau einmal in yes ein und gibt dann die Anzahl der gefundenen Buchstaben zurück
def partone(line_input):
    yes = []
    for j in range(len(line_input)):
        for c in line_input[j]:
            if c not in yes:
                yes.append(c)
    return len(yes)

# Fügt alle Buchstaben, die in allen Strings im Input vorkommen, in every_yes ein und gibt die Anzahl der gefundenen Buchstaben zurück
def parttwo(line_input):
    every_yes = []
    for c in line_input[0]:
        exists = 1
        j = 1
        while j < len(line_input):
            if c in line_input[j]:
                exists += 1
            j += 1
        if exists == len(line_input) and c not in every_yes:
            every_yes.append(c)
    return len(every_yes)

# Zeilenumbrüche entfernen
for i in range(len(lines)):
    lines[i] = lines[i].split('\n')

p1count = 0
for line in lines:
    p1count += partone(line)
print(p1count)

p2count = 0
for line in lines:
    p2count += parttwo(line)
print(p2count)
