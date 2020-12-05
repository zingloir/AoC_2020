with open('input') as f:
    numbers = f.read().split('\n')

def checktwonumber(number, pos):
    i = pos
    while i < len(numbers):
        if int(number) + int(numbers[i]) == 2020:
            return int(number) * int(numbers[i])
        i += 1
    return 0

def checkthreenumber(number, pos):
    i = pos
    while i < len(numbers):
        j = i
        while j < len(numbers):
            if int(number) + int(numbers[i]) + int(numbers[j]) == 2020:
                return int(number) * int(numbers[i]) * int(numbers[j])
            j += 1
        i += 1
    return 0


k = 0
while k < len(numbers):
    temp = checktwonumber(numbers[k], k)
    if temp > 0:
        print(temp)
        break
    k += 1

k = 0
while k < len(numbers):
    temp = checkthreenumber(numbers[k], k)
    if temp > 0:
        print(temp)
        break
    k += 1
