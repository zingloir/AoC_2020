import copy

def program():
    lines = get_input()
    j1, j3 = count_adapters(lines)
    print("Produkt aus der Anzahl aus 1 und 3 Jolt Unterschieden: " + str(j1 * j3))
    count_arrangements(lines)


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
    highest = max(lines)
    print(combo_checker(0, lines))


def combo_checker(jolt, lines):
    hitcounter = 0
    if jolt < max(lines):
        if jolt + 1 in lines:
            hitcounter += combo_checker(jolt + 1, lines)
        if jolt + 2 in lines:
            hitcounter += combo_checker(jolt + 2, lines)
        if jolt + 3 in lines:
            hitcounter += combo_checker(jolt + 3, lines)
    else:
        hitcounter += 1
    return hitcounter


# Programm
program()
