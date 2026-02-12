import os

# Hole den aktuellen Benutzernamen vom Betriebssystem
current_user = os.getlogin()

# Benutze den Namen in einer persönlichen Begrüßung
print(f"Hallo, {current_user}!")
dienst = input(f"Welcher Dienst soll geprüft werden, {current_user}? ")
if dienst == "apache2":
    print("Der Webserver (apache2) läuft.")
elif dienst == "ssh":
    print("Der SSH-Dienst ist aktiv.")
else: 
    print(f"FEHLER: Der Dienst '{dienst}' ist unbekannt.")