#!/usr/bin/env python3
"""
Ein einfaches Kommandozeilen-Tool (CLI), das als Aufräum-Helfer dient.

Das Skript ist in Funktionen strukturiert, um die Lesbarkeit und
Wiederverwendbarkeit des Codes zu demonstrieren. Es listet alle
.txt-Dateien in einem vordefinierten Ordner auf.

Version 2: Enthält einen Shebang für Linux und nutzt dynamische Pfade,
um Sicherheit und Portabilität zu gewährleisten.
"""

# Importe stehen immer ganz am Anfang des Skripts.
import os

# --- Funktionsdefinitionen ---

def begruessung_anzeigen():
    """Gibt eine einfache Startnachricht auf der Konsole aus."""
    print("--- Aufräum-Helfer gestartet ---")

def finde_text_dateien():
    """Durchsucht einen Zielordner und listet alle .txt-Dateien auf."""
    
    # --- Professionelle Pfad-Erstellung (Sicher & Portabel) ---
    # Anstatt den Pfad festzuschreiben, bauen wir ihn dynamisch zusammen.
    
    # 1. Finde das Home-Verzeichnis des aktuellen Benutzers (z.B. '/home/thommesw').
    #    os.path.expanduser('~') ist der sichere Weg, dies zu tun.
    home_verzeichnis = os.path.expanduser('~')
    
    # 2. Verbinde das Home-Verzeichnis mit unserem Ziel-Unterordner.
    #    os.path.join() baut den Pfad systemkorrekt zusammen (mit / auf Linux).
    ziel_ordner = os.path.join(home_verzeichnis, "lpic-lernen")
    
    print(f"Durchsuche Ordner: {ziel_ordner}") # Feedback für den User
    
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
# Das eigentliche Programm beginnt hier.
begruessung_anzeigen()
finde_text_dateien()
