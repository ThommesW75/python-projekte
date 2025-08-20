"""
Ein interaktives Kommandozeilen-Programm zur Verwaltung einer Einkaufsliste.

Das Programm ermöglicht es dem Benutzer, Artikel zu einer Liste hinzuzufügen
und sie wieder zu entfernen. Es ist robust gebaut und fängt Fehleingaben ab,
um einen Programmabsturz zu verhindern.
"""

# Wir starten mit einer leeren Liste, die unsere Artikel aufnehmen wird.
einkaufsliste = []

# Die while True-Schleife sorgt dafür, dass das Menü immer wieder angezeigt wird.
while True:
    # \n sorgt für einen Zeilenumbruch und damit für eine saubere Optik.
    # Wir geben bei jeder Wiederholung die aktuelle Liste aus.
    print(f"\nAktuelle Liste: {einkaufsliste}")
    print("1. Artikel hinzufügen | 2. Artikel entfernen | 3. Beenden")

    # Wir holen die Eingabe des Benutzers. Das Ergebnis ist immer ein String.
    wahl = input("Deine Wahl: ")

    # --- Logik zur Verarbeitung der Benutzereingabe ---

    # Fall 1: Der Benutzer möchte einen Artikel hinzufügen.
    if wahl == "1":
        neuer_artikel = input("Welcher Artikel soll hinzugefügt werden? ")
        # Die .append()-Methode fügt das Element am Ende der Liste hinzu.
        einkaufsliste.append(neuer_artikel)
        print(f'"{neuer_artikel}" wurde zur Liste hinzugefügt.')

    # Fall 2: Der Benutzer möchte einen Artikel entfernen.
    elif wahl == "2":
        artikel_entfernen = input("Welcher Artikel soll entfernt werden? ")
        
        # WICHTIG: Erst prüfen, ob der Artikel überhaupt in der Liste ist.
        # Das verhindert einen Absturz (ValueError), falls er nicht existiert.
        if artikel_entfernen in einkaufsliste:
            # Die .remove()-Methode entfernt das erste Vorkommen des Elements.
            einkaufsliste.remove(artikel_entfernen)
            print(f'"{artikel_entfernen}" wurde von der Liste entfernt.')
        else:
            # Freundliches Feedback, wenn der Artikel nicht gefunden wurde.
            print(f'"{artikel_entfernen}" steht nicht auf der Einkaufsliste.')

    # Fall 3: Der Benutzer möchte das Programm beenden.
    elif wahl == "3":
        print("Programm wird beendet.")
        # break beendet die while-Schleife und damit das Programm.
        break

    # Fall 4: Der Benutzer hat etwas Ungültiges eingegeben.
    else:
        print(">>> Ungültige Eingabe! Bitte nur 1, 2 oder 3 wählen. <<<")
            
