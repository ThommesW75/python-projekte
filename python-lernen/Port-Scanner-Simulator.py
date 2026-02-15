offen = [22, 80, 443]
for i in range(1000):
    if i in offen:
        print(f"Port {i} ist OFFEN (Kritischer Dienst!)")


