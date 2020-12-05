with open("input") as f:
    seats = f.readlines()


# Binärzahl in Dezimalzahl umwandeln
def bintodec(binary):
    dec = 0
    binary = int(binary)
    i = 0
    while binary != 0:
        rest = binary % 10
        dec += rest * (2 ** i)
        binary //= 10
        i += 1
    return dec


# Platznummern berechnen
def calcseat(seat):
    row = bintodec(seat[:7])
    col = bintodec(seat[7:])
    return row * 8 + col


# Input anpassen
for i in range(len(seats)):
    seats[i] = seats[i].rstrip("\n")
    seats[i] = seats[i].replace('F', '0')
    seats[i] = seats[i].replace('L', '0')
    seats[i] = seats[i].replace('B', '1')
    seats[i] = seats[i].replace('R', '1')

# Höchste Platznummer suchen und ausgeben, Sitznummer in numbers schreiben
high = 0
numbers = []
for seat in seats:
    # Aufgabe Teil 1
    num = calcseat(seat)
    numbers.append(num)
    if num > high:
        high = num
print("Höchste Platznummer:", high)

# Aufgabe Teil 2, eigene Platznummer finden
i = 1
while i < high:
    if i not in numbers:
        if i - 1 in numbers and i + 1 in numbers:
            print("Eigener Sitzplatz:", i)
    i += 1
