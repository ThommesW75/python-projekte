def rechnen(zahl1, zahl2, zahl3):

    i = 0
    zwischenergebnis = []

    while i < zahl3:
        zwischenergebnis.append(zahl1 + zahl2 + i)
        i += 1
    return zwischenergebnis

def ausgabe(wert):

    for zahl in wert:
        print(zahl, end = "\t")
    print()

a = 3
b = 4
c = 5

for aktuelles_a in range(a, c):
    ergebnis = rechnen(aktuelles_a, b, c)
    ausgabe(ergebnis)
