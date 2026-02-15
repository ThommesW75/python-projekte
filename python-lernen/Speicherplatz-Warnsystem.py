auslastung = [15, 45, 92, 78, 98]

server_nummer = 1

for i in auslastung:
    if i > 90:
        print(f"KRITISCH: Bei Server {server_nummer} sofort handeln!")
    elif i > 70:
        print(f"Warnung: Der Speicherplatz von {server_nummer} wird knapp.")
    else:
        print(f" Server {server_nummer} OK.")

    server_nummer = server_nummer + 1
