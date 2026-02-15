while True:
    pwd = input("Bitte gebe dein Passwort ein:")

    if pwd == "geheim123":
        print("Zugang erlaubt.")
        break

    else:
        print("Passwort falsch! Bitte probieren sie es erneut.")

print("Programm beendet.")