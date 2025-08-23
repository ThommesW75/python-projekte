#!/usr/bin/env python3
"""
Ein Skript zur automatischen Synchronisierung von Lernstand-Dateien
in themenspezifische, komprimierte tar.gz-Archive.

Das Skript nutzt einen robusten "Dekomprimieren -> Aktualisieren ->
Neu Komprimieren"-Workflow, um die Einschränkungen des tarfile-Moduls
mit komprimierten Archiven zu umgehen.
"""

import os
import tarfile
import shutil # Importieren wir das Modul für Dateioperationen

# --- Globale Konfiguration ---
KONFIGURATION = [
    {
        'ordner': 'AWS',
        'archiv': 'AWS_Lernstand.tar.gz',
        'praefix': 'AWS_History_'
    },
    {
        'ordner': 'python_PCEP',
        'archiv': 'PCEP_Lernstand.tar.gz',
        'praefix': 'PCEP_History_'
    },
    {
        'ordner': 'LPIC-1',
        'archiv': 'LPIC-101_Lernstand.tar.gz',
        'praefix': 'LPIC-101_History_'
    }
]

# --- Helfer-Funktionen ("Mitarbeiter") ---

def hole_basis_pfad():
    """Ermittelt den Pfad zum Basisordner 'Umschulung'."""
    home_verzeichnis = os.path.expanduser('~')
    return os.path.join(home_verzeichnis, "Umschulung")

def synchronisiere_archiv(quellordner, archiv_pfad, datei_praefix):
    """
    Sucht nach neuen Dateien und aktualisiert das komprimierte Archiv.
    """
    print(f"\n--- Prüfe Ordner: {os.path.basename(quellordner)} ---")
    
    # 1. Eine Liste aller zu archivierenden .txt-Dateien im Quellordner erstellen
    zu_archivierende_dateien = []
    for eintrag in os.listdir(quellordner):
        if eintrag.startswith(datei_praefix) and eintrag.endswith(".txt"):
            voller_pfad = os.path.join(quellordner, eintrag)
            zu_archivierende_dateien.append(voller_pfad)

    # Wenn keine neuen Dateien gefunden wurden, müssen wir nichts tun.
    if not zu_archivierende_dateien:
        print("-> Keine neuen Lernstand-Dateien gefunden.")
        return # Beendet die Funktion für diesen Ordner

    # --- Der robuste Update-Prozess ---
    
    # 2. Temporären Ordner für das Update erstellen
    temp_ordner = os.path.join(quellordner, "temp_archiv_update")
    os.makedirs(temp_ordner, exist_ok=True) # exist_ok=True verhindert Fehler, wenn er schon da ist

    # 3. Bestehendes Archiv in den temporären Ordner entpacken (falls es existiert)
    if os.path.exists(archiv_pfad):
        print(f"-> Entpacke bestehendes Archiv '{os.path.basename(archiv_pfad)}'...")
        with tarfile.open(archiv_pfad, "r:gz") as archiv:
            archiv.extractall(path=temp_ordner)

    # 4. Neue Dateien in den temporären Ordner kopieren (überschreibt alte Versionen)
    for datei_pfad in zu_archivierende_dateien:
        print(f"-> Aktualisiere mit '{os.path.basename(datei_pfad)}'...")
        shutil.copy(datei_pfad, temp_ordner)

    # 5. Altes Archiv löschen und aus dem temporären Ordner neu erstellen
    if os.path.exists(archiv_pfad):
        os.remove(archiv_pfad)
    
    print(f"-> Erstelle neues Archiv '{os.path.basename(archiv_pfad)}'...")
    with tarfile.open(archiv_pfad, "w:gz") as neues_archiv:
        # Wir müssen den Pfad anpassen, damit im Archiv keine Ordnerstruktur entsteht
        for datei in os.listdir(temp_ordner):
            pfad_in_temp = os.path.join(temp_ordner, datei)
            neues_archiv.add(pfad_in_temp, arcname=datei)

    # 6. Verifizieren und Aufräumen
    print("-> Verifiziere und räume auf...")
    with tarfile.open(archiv_pfad, "r:gz") as archiv:
        inhalt = archiv.getnames()
        for datei_pfad in zu_archivierende_dateien:
            dateiname = os.path.basename(datei_pfad)
            if dateiname in inhalt:
                os.remove(datei_pfad) # Original löschen
                print(f"   -> Erfolg! Originaldatei '{dateiname}' wurde gelöscht.")
            else:
                print(f"   -> FEHLER! '{dateiname}' konnte nicht im neuen Archiv verifiziert werden!")

    # 7. Temporären Ordner löschen
    shutil.rmtree(temp_ordner)


def main():
    """Die Haupt-Steuerungsfunktion des Skripts."""
    print("Starte Archiv-Synchronisierer...")
    basis_pfad = hole_basis_pfad()

    for config in KONFIGURATION:
        quellordner_pfad = os.path.join(basis_pfad, config['ordner'])
        archiv_pfad = os.path.join(quellordner_pfad, config['archiv'])
        
        synchronisiere_archiv(quellordner_pfad, archiv_pfad, config['praefix'])
    
    print("\nAlle Aufgaben abgeschlossen.")

if __name__ == "__main__":
    main()

    

