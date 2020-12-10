def count_adapters():
    step1 = 0
    step3 = 0
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


with open('input') as f:
    lines = f.read().split('\n')

for i in range(len(lines)):
    lines[i] = int(lines[i])
    i += 1

lines.append(0)
lines.append(max(lines) + 3)
lines = sorted(lines)

j1, j3 = count_adapters()
print("Produkt aus der Anzahl aus 1 und 3 Jolt Unterschieden: " + str(j1 * j3))

# Dreist geklaut, Part 2
poss = [1] + [0] * lines[-1]
for i in lines[1:]:
    poss[i] = poss[i - 1] + poss[i - 2] + poss[i - 3]
print(poss[-1])
