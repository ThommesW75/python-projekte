while True:
    print("--- Menu ---")
    print("Systemstatus prüfen")
    print("Benutzer auflisten")
    print("Beenden")

    auswahl = int(input("Bitte wählen Sie aus: "))

    if auswahl == 1:
        print("System wird geprüft...")
    elif auswahl == 2:
        print("Nach Benutzern wird gesucht...")
    elif auswahl == 3:
        print("Auf wiedersehen.")
        break
    else:
        print("Ungültige Eingabe!")

print("Programm beendet.")
