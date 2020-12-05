input = []
with open("input") as f:
    input = list(f.readlines())

i = 0
cor = 0
wro = 0

while i < len(input) - 1:
    str = input[i]
    a = int(str[:str.find("-")])
    b = int(str[str.find("-") + 1:str.find(" ")])
    ges = str[str.find(" ") + 1]
    count = 0
    j = str.find(":") + 2
    while j < len(str) - 1:
        if str[j] == ges:
            count = count + 1
        j = j + 1
    if count >= a and count <= b:
        cor = cor + 1
    else:
        wro = wro + 1
    i = i + 1
print(cor)
print(wro)

i = 0
count = 0
while i < len(input) - 1:
    str = input[i]
    a = int(str[:str.find("-")])
    b = int(str[str.find("-") + 1:str.find(" ")])
    ges = str[str.find(" ") + 1]
    j = str.find(":") + 1
    if str[j + a] == ges or str[j + b] == ges:
        if str[j + a] == ges and str[j + b] == ges:
            i = i + 1
            continue
        count = count + 1
    i = i + 1
print(count)