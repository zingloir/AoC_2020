import copy

def program():
    lines = get_input()
    j1, j3 = count_adapters(lines)
    print("Produkt aus der Anzahl aus 1 und 3 Jolt Unterschieden: " + str(j1 * j3))
#    print(str(count_arrangements(lines)))


def get_input():
    with open('input') as f:
        lines = f.read().split('\n')

    for i in range(len(lines)):
        lines[i] = int(lines[i])
        i += 1

    return lines


def count_adapters(lines):
    step1 = 0
    step3 = 1
    jolt = 0

    while jolt < max(lines):
        if jolt + 1 in lines:
            step1 += 1
            jolt += 1
        elif jolt + 2 in lines:
            jolt += 2
        elif jolt + 3 in lines:
            step3 += 1
            jolt += 3
    return step1, step3


def count_arrangements(lines):
    combos = [[0]]
    for i in range(len(combos)):
        while max(combos[i]) < max(lines):
            combos = find_nextsteps(lines, combos, combos[i])
    return len(combos)


def find_nextsteps(lines, combos, combo):
    i = 1
    while i <= 3:
        if check_if_exists(i, combo, lines) is False:
            i += 1
        else:
            combos.append(check_if_exists(i, combo, lines))
            i += 1
    combos.remove(combo)
    print(len(combo))
    return combos


def check_if_exists(step, combo, lines):
    testline = copy.deepcopy(combo)
    jolt = max(testline)
    if jolt + step in lines:
        testline.append(jolt + step)
        return testline
    return False

# Programm
program()
