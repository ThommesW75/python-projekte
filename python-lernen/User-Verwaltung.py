admins = ["Thomas"]

while True:

    print("\n --- Menü --- ")
    print("1. ADMIN hinzufügen")
    print("2. ADMIN entfernen")
    print("3. Liste anzeigen")
    print("4. Programm beenden")

    eingabe = int(input("Bitte geben sie eine wählen Sie (1-4):"))
    if eingabe == 1:
        admins.append(input("Wer soll mit in die Liste aufgenommen werden?"))
    elif eingabe == 2:
        admins.remove(input("Wer soll aus der Liste?"))
    elif eingabe == 3:
        print(f"ADMINS: {admins}")
    elif eingabe == 4:
        break
    else:
        print("Falsche Eingabe!")

print("Programm beendet.")

