"""
Ein einfaches Kommandozeilen-Tool (CLI), das als Projekt-Starter dient.

Das Programm zeigt ein interaktives Menü in einer Endlosschleife an
und reagiert auf die Eingaben des Benutzers, bis dieser das Programm
explizit beendet. Es gibt Feedback bei ungültigen Eingaben.
"""

# Die while True-Anweisung startet eine Schleife, die ohne einen break-Befehl
# unendlich weiterlaufen würde.
while True:
    # Der Menü-Text wird bei jeder Wiederholung der Schleife neu angezeigt.
    print("\n--- Hauptmenü ---") # Ein \n am Anfang sorgt für etwas Abstand.
    print("1. Neues Projektverzeichnis anlegen")
    print("2. Beenden")

    # Wir holen die Eingabe des Benutzers und speichern sie in der Variable 'wahl'.
    wahl = input("Deine Wahl: ")

    # Wir prüfen, ob der Inhalt der Variable 'wahl' der Zeichenkette "2" entspricht.
    if wahl == "2":
        print("Programm wird beendet...")
        # Der break-Befehl beendet die Schleife sofort.
        break
    # Falls die erste Bedingung nicht zutrifft, prüfen wir, ob 'wahl' gleich "1" ist.
    elif wahl == "1":
        # Dies ist aktuell ein Platzhalter. In Zukunft könnte hier Code stehen,
        # der z.B. mit dem os-Modul ein Verzeichnis erstellt.
        print("Platzhalter: Projektverzeichnis wird erstellt...")
    # Der else-Block fängt alle anderen Fälle ab, die nicht "1" oder "2" sind.
    else:
        print(">>> Ungültige Eingabe! Bitte nur 1 oder 2 wählen. <<<")
