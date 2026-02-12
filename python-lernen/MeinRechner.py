import random

class MeinRechner:
    # Das ist der Konstruktor.
    # 'self' ist wie ein Namensschild am Koffer: "Das gehört zu MIR."
    def __init__(self, a, b):
        self.a = a  # Erschafft die Variable a
        self.b = b  # Erschafft die Variable b
        self.c = 0        # Erschafft die Variable c

    # Eine einfache Methode
    def addieren(self):
        for i in range(5):
            self.c = self.a + self.b
            print(f"Ergebnis in Durchgang {i + 1} der Addition: {self.c}")
            self.a +=1  

    def multiplizieren(self):
        j = 5
        while j < 10:
            d = self.a * self.c
            print(f"Ergebnis in Durchgang {j + 1} der Multiplikation: {d}")
            self.c +=1
            j +=1

# Direktes "Füttern" des Objekts
mein_objekt = MeinRechner(random.randint(1, 10), random.randint(1, 10))

# Wir rufen die Methode auf
mein_objekt.addieren()
mein_objekt.multiplizieren()

