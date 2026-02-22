def begruessung(name):
    text = f"Hallo {name}, das System ist bereit für dich."
    return text

familie = ["Tina", "Luki", "Lenni"]

for mitglied in familie:
    ergebnis = begruessung(mitglied)
    print(ergebnis)