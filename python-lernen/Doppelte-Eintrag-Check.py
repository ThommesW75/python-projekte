bekannte_ips = ["192.168.1.1", "192.168.1.10", "192.168.1.20"]

schon_vorhanden = False

neue_ip = input("Welche IP soll hinzugefügt werden? ")

for ip in bekannte_ips:
    if ip == neue_ip:
        schon_vorhanden = True
        break

if schon_vorhanden:
    print(f" {neue_ip} bereits vorhanden.")

else:
    bekannte_ips.append(neue_ip)
    print(f" {neue_ip} wurde hinzugefügt.")
    print(bekannte_ips)
