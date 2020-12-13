import timeit
start = timeit.default_timer()

# Bereinigt Input
# depart: Früheste Abfahrtzeit für Part 1
# lines: Enthält allen Input aus Zeile 2 des Inputs, gesplitet an den Kommas
with open('input') as f:
    lines = f.read().split('\n')
    depart = int(lines.pop(0))
    lines = lines[0].split(',')

# Part 1
# Berechnet nächsten Abfahrtszeitpunkt für jeden Bus ab dem frühestmöglichen Zeitpunkt in depart
nextdepart = []
for bus in lines:
    if bus != 'x':
        nextdepart.append([int(bus), int(bus) * ((depart // int(bus)) + 1)])

next_time = min(nextdepart[i][1] for i in range(len(nextdepart)))
next_bus = 0
while True:
    if nextdepart[next_bus][1] == next_time:
        next_bus = int(nextdepart[next_bus][0])
        break
    next_bus += 1

print((next_time - depart) * next_bus)

# Part 2
# Mal wieder geklaut. Meine Lösung hätte funktioniert, aber nur mit unrealistischer Laufzeit
# i = off
# k = busid
# t = time
def mod_inverse(a, n):
    a = a % n
    for x in range(1, n ):
        if (a * x) % n == 1:
            return x
    return 1


def earliest():
    ids = []
    fullProduct = 1
    for off in range(len(lines)):
        item = lines[off]
        if item != 'x':
            busid = int(item)
            off = off % busid
            ids.append(((busid - off) % busid, busid))
            fullProduct *= busid

    total = 0
    for off, busid in ids:
        partialProduct = fullProduct // busid

        inverse = mod_inverse(partialProduct, busid)
        assert (inverse * partialProduct) % busid == 1

        term = inverse * partialProduct * off
        total += term

    return total % fullProduct

print(earliest())
