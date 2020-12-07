import re
with open ('input') as f:
    lines = f.readlines()


# Sucht alle Taschen, die direkt oder indirekt target_col enthalten, Funde werden in checked_true gespeichert
# Wird rekursiv aufgerufen, bis Tasche ohne "Untertaschen" gefunden wird
def findbags(src_col):
    for j in range(len(bags)):
        if bags[j][0][1] == src_col:
            found = False
            k = 1
            while k < len(bags[j]):
                if bags[j][k][1] in checked_true:
                    found = True
                elif bags[j][k][1] == target_col:
                    found = True
                elif findbags(bags[j][k][1]):
                    found = True
                k += 1
                if found and bags[j][0][1] not in checked_true:
                    checked_true.append(bags[j][0][1])
            return found
    return False


# Zählt Anzahl der Taschen in Tasche mit Farbe src_col inkl. Untertaschen
# Wird rekursiv aufgerufen, bis tiefste Tasche erreicht wird. Gibt Anzahl der enthaltenen Taschen zurück,
# inklusive sich selbst
def get_numbers(src_col):
    for j in range(len(bags)):
        if bags[j][0][1] == src_col:
            if src_col == target_col:
                counter = 0
            else:
                counter = 1
            k = 1
            while k < len(bags[j]):
                counter += get_numbers(bags[j][k][1]) * int(bags[j][k][0])
                k += 1
            return counter


# Input bereinigen
bags = [''] * len(lines)
pattern = '([0-9])? ?([a-z]+ [a-z]+)'
remove = (' contain no other bags.', ' contain ', ' bags ', ' bag ', ', ', '.')

for i in range(len(lines)):
    for r in remove:
        lines[i] = lines[i].replace(r, '')
    bags[i] = re.findall(pattern, lines[i])


# Taschen suchen, die direkt oder indirekt target_col enthalten
target_col = 'shiny gold'
checked_true = []
for i in range(len(bags)):
    findbags(bags[i][0][1])

print('Bags, die direkt oder indirekt ' + target_col + ' Bags enthalten: ' + str(len(checked_true)))
print('Bags innerhalb eines ' + target_col + ' Bags: ' + str(get_numbers(target_col)))
