server_liste = ["Web-01", "DB-01", "Mail-01", "Backup-01", "Proxy-01"]

suche = input("Welchen Server suchen Sie? ")

gefunden = False

for server in server_liste:
    if server == suche:
        print(f"{server} wurde gefunden!")
        gefunden = True
        break

if gefunden == False:
    print("Server nicht im System bekannt.")