# --- Schritt 1: Den leeren Behälter vorbereiten ---
# Wir erstellen eine leere Liste, um die Benutzernamen zu sammeln.
neue_benutzer = []

# --- Schritt 2: Den Motor starten ---
# 'while True:' startet eine Endlosschleife. Wir verlassen sie später
# gezielt mit dem 'break'-Befehl.
while True:
    # --- Schritt 3: Den Benutzer zur Eingabe auffordern ---
    # Bei jeder Wiederholung der Schleife fragen wir nach einer neuen Eingabe.
    eingabe = input("Neuen Benutzernamen eingeben (oder 'ende' zum Beenden): ")

    # --- Schritt 4: Die Abbruchbedingung prüfen ---
    # Wir prüfen, ob der Benutzer das Schlüsselwort zum Beenden eingegeben hat.
    if eingabe == "ende":
        # Wenn ja, wird die 'while'-Schleife sofort abgebrochen.
        break
    else:
        # --- Schritt 5: Den Benutzernamen zur Liste hinzufügen ---
        # Wenn nicht 'ende' eingegeben wurde, hängen wir die Eingabe
        # an unsere Liste an.
        neue_benutzer.append(eingabe)

# --- Schritt 6: Das Endergebnis ausgeben ---
# Dieser Code wird erst erreicht, nachdem die Schleife beendet wurde.
print(f"\nFolgende Benutzer werden angelegt: {neue_benutzer}")