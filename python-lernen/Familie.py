class Familie:

    def __init__(self, name, alter, geschlecht):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht

    def vorstellung(self):

        if self.geschlecht == "männlich":
            if self.alter >= 50:
                print(f" Vater {self.name} ist {self.alter} Jahre alt.")
            else:
                print(f" Sohn {self.name} ist {self.alter} Jahre alt.")

        else:
            print(f" Mutter {self.name} ist {self.alter} Jahre alt.")


def main():

    family = [Familie("Thomas", 50, "männlich" ),
            Familie("Tina", 46, "weiblich"),
            Familie("Lukas", 23, "männlich"),
            Familie("Lenni", 18, "männlich"),]

    for mitglied in family:
        mitglied.vorstellung()

if __name__ == "__main__":
    main()

