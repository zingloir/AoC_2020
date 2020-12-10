with open('testinput') as f:
    l = [int(x) for x in f.readlines()]
l.append(0)
l.append(max(l) + 3)
l = sorted(l)
cache = {}
def calc(i):
    if i in cache:
        return cache[i]
    if i == len(l) - 1:
        return 1
    acc = 0
    for a in range(i + 1, len(l)):
        if l[a] - l[i] <= 3:
            acc += calc(a)
    cache[i] = acc
    return acc
def p1():
    print(calc(0))
p1()