tickets = ["Offen", "Geschlossen", "Offen", "In Bearbeitung", "Offen"]
nummer = 1
for status in tickets:
    if status == "Offen":
        print(f"Ticket {nummer} ist noch offen")
    nummer +=1
    