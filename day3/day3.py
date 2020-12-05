# Input aus Datei einlesen und Zeilenumbrüche entfernen
with open("slope") as f:
    slope = f.readlines()
    for i in range(len(slope)):
        slope[i] = slope[i].rstrip("\n")

# Liste steps für die unterschiedlichen Bewegungsarten mit Schrittweite auf x und y Achse 
# i Zählvariable für Durchgang mit jeder Variante aus steps
# parttwo für Produkt aus Gesamtzahl der Bäume aus jedem Durchgang
steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
i = 0
parttwo = 0

while i < len(steps):
    # x und y für Position in slope
    x = 0
    y = 0
    trees = 0
    # Solange mit dem folgenden Schritt nicht das Ende der Karte überschritten wird
    while y < len(slope) - steps[i][1]:
        # x gemäß Durchgang in steps inkrementieren, falls es über den Kartenrand rausgeht,
        # dann die Länge der Zeile abziehen, um wieder von links anzufangen
        x += steps[i][0]
        if x >= len(slope[y]):
            x -= len(slope[y])
        # y gemäß Durchgang in steps inkrementieren
        y += steps[i][1]
        # Prüfung, ob an der x y Position in slope ein Baum bzw. # ist
        if slope[y][x] == "#":
            trees += 1
    # Ausgabe der gefundenen Bäume
    print("Gefundene Bäume: ", trees, " in Durchgang: ", i)
    # Berechnung für zweiten Teil der Aufgabe
    if parttwo == 0:
        parttwo = trees
    else:
        parttwo = parttwo * trees
    i += 1
# Ausgabe Teil 2
print("Gesamte Bäume: ", parttwo)
