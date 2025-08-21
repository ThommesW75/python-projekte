"""
Ein einfaches Kommandozeilen-Tool (CLI), das als Aufräum-Helfer dient.

Das Skript ist in Funktionen strukturiert, um die Lesbarkeit und
Wiederverwendbarkeit des Codes zu demonstrieren. Es listet alle
.txt-Dateien in einem vordefinierten Ordner auf.
"""

# Importe stehen immer ganz am Anfang des Skripts.
# Wir importieren das os-Modul, um mit dem Betriebssystem zu interagieren.
import os

# --- Funktionsdefinitionen ---
# Hier definieren wir unsere Werkzeuge (unsere Funktionen).
# Dieser Code wird erst ausgeführt, wenn die Funktionen später aufgerufen werden.

def begruessung_anzeigen():
    """Gibt eine einfache Startnachricht auf der Konsole aus."""
    print("--- Aufräum-Helfer gestartet ---")

def finde_text_dateien():
    """Durchsucht einen Zielordner und listet alle .txt-Dateien auf."""
    
    # Der Pfad zum Ordner, der durchsucht werden soll.
    ziel_ordner = "/home/thommesw/lpic-lernen/"
    
    # os.listdir() gibt eine Liste aller Dateien und Ordner im Zielordner zurück.
    alle_eintraege = os.listdir(ziel_ordner)
    
    print("\nGefundene .txt-Dateien:")
    
    # Wir gehen die Liste der Einträge mit einer for-Schleife durch.
    for eintrag in alle_eintraege:
        # Die String-Methode .endswith() prüft, ob der Text mit ".txt" endet.
        if eintrag.endswith(".txt"):
            # Wenn ja, geben wir den Namen des Eintrags aus.
            print(eintrag)

# --- Hauptprogramm ---
# Das eigentliche Programm beginnt hier. Der Code wird von oben nach unten ausgeführt.
# Wir rufen unsere zuvor definierten Funktionen in der gewünschten Reihenfolge auf.

begruessung_anzeigen()
finde_text_dateien()
