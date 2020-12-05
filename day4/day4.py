import re
lines = []
with open ("input") as f:
    lines = f.readlines()

lines.append('\n')
pattern = re.compile("([a-z]+):(#?[0-9a-z]+)[ \n]")
heightpattern = (r"^([0-9]+)([a-z]+)$")
hclpattern = (r"#([0-9a-f]{6})")
pidpattern = (r"^(\d{9})$")
p1validCounter = 0
p2validCounter = 0
passport = ""
match = ''
ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
values = ['','','','','','','','']
valid = True

# Line für Line einlesen, bis eine leere Zeile gefunden wird
for line in lines:
    if line != "\n" and line != "":
        match = pattern.findall(line)
        for stat in match:
            i = 0
            while i < len(fields):
                if stat[0] == fields[i]:
                    fields[i] = ''
                    # Part Two
                    values[i] = stat[1]
                i += 1
    else:
        # Prüfen ob alle nötigen Felder vorhanden sind
        i = 0
        while i < len(fields):
            if fields[i] != '':
                if fields[i] == 'cid':
                    i += 1
                else:
                    valid = False
                    break
            i += 1
        if valid:
            p1validCounter += 1

        # Part Two
            # Birth Year / byr
            if not 1920 <= int(values[0]) <= 2002:
                valid = False
            # Issue Year / iyr
            if not 2010 <= int(values[1]) <= 2020:
                valid = False
            # Expiration Year / eyr
            if not 2020 <= int(values[2]) <= 2030:
                valid = False
            # Height / hgt
            height = re.match(heightpattern, values[3])
            if height is None:
                valid = False
            elif height.group(2) == "in":
                if not 59 <= int(height.group(1)) <= 76:
                    valid = False
            elif not 150 <= int(height.group(1)) <= 193:
                valid = False
            # Hair Color / hcl
            hair = re.search(hclpattern, values[4])
            if hair is None:
                valid = False
            # Eye Color / ecl
            if not values[5] in ecls:
                valid = False
            # Passport ID / pid
            passport = re.search(pidpattern, values[6])
            if passport is None:
                valid = False
        if valid:
            p2validCounter += 1
        else:
            valid = True
        fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        values = ['', '', '', '', '', '', '', '']
        match = ''
print("Gültige Ausweise P1:", p1validCounter)
print("Gültige Ausweise P2:", p2validCounter)
