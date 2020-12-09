# Programmablauf
def program():
    clean_input()
    fail = (check_lines(25))
    print("Fehlerhafte Zahl: " + str(fail))
    print("Weakness: " + str(find_sum(fail)))


# Listenelemente in Integer konvertieren
def clean_input():
    for i in range(len(lines)):
        lines[i] = int(lines[i])


# Prüft alle Lines, bis fehlerhafte Zeile gefunden wurde
def check_lines(preamble):
    i = preamble
    while i < len(lines):
        if check_pos(i, preamble):
            i += 1
        else:
            return lines[i]
    return False


# Prüft angegebene Position, ob sie sich aus einer Summe von 2 aus der in preamble übergebenen range in lines bilden lässt
def check_pos(pos, preamble):
    j = 1
    while j < preamble:
        if lines[pos] - lines[pos - j] in lines[pos - preamble:pos]:
            return True
        j += 1
    return False


# Sucht nach einer Range, aus der sich die Zahl fail addieren lässt, gibt die Summe aus
# der kleinsten und größten Zahl dieser Range zurück
def find_sum(fail):
    i = 0
    while lines[i] != fail:
        j = 0
        while j < i:
            k = j
            sum = 0
            while k < i:
                sum += lines[k]
                if sum == fail:
                    return min(lines[j:k + 1]) + max(lines[j:k + 1])
                elif sum >= fail:
                    break
                else:
                    k += 1
            j += 1
        i += 1


# Input einlesen
with open ("input") as f:
    lines = f.read().split('\n')

# Programm ausführen
program()
