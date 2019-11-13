betrag = int(input('Geld bitte!'))
kosten = int(input('kosten von Produkt'))
rueckgeld = betrag - kosten
geld_scheine = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for schein in geld_scheine:
    if rueckgeld > schein:
        print('du bekommst ' + str(int(rueckgeld/schein)) + ' mal ' + str(schein) + ' euro')
        rueckgeld -= int(rueckgeld/schein)*schein