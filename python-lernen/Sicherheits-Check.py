services = ["Datenbank", "Webserver", "Speicher", "Firewall"]

alles_ok = True

for service in services:
    status = input(f" Dienst {service} aktiv? (Ja/Nein)").lower()
    if status == "nein":
        alles_ok = False

if alles_ok:
    print("System-Status: BEREIT")

else:
    print("System-Status: FEHLER - Bitte Techniker rufen")