laufzeiten = []
i = 0
while i < 3:
    laufzeiten.append(int(input("Nenne mir bitte eine deiner letzten Zeiten in Minuten:")))
    i += 1
print(f"Das waren deine letzten 3 Zeiten {laufzeiten}")
print(f"Insgesamt bis du {sum(laufzeiten)} Minuten gelaufen.")
print(f"Dein durchschnittliche Laufzeit betrug {sum(laufzeiten)/len(laufzeiten)} Minuten.")
