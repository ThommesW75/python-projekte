class Familienmitglied:
    def __init__(self, name, rolle, alter):
        self.name = name
        self.rolle = rolle
        self.alter = alter

    def vorstellung(self):

        print(f" {self.rolle} {self.name} ist {self.alter} Jahre alt.")


# Objekte erstellen
thomas = Familienmitglied("Thomas", "Vater", 50)
tina = Familienmitglied("Kristina", "Mutter", 46)
lukas = Familienmitglied("Lukas", "Sohn", 23)
lenni = Familienmitglied("Lennart", "Sohn", 18)

# Alle Personen in einer Liste sammeln
meine_familie = [thomas, tina, lukas, lenni]

# Mit einer Schleife alle vorstellen
for person in meine_familie:
    person.vorstellung()