def gb_zu_mb(anzahl_gb):
    return anzahl_gb * 1024

def main():

    gigabyte = int(input(" Wie viele GB soll ich in MB umrechnen ? "))

    ergebnis = gb_zu_mb(gigabyte)
    print(f" {gigabyte} GB entsprechen {ergebnis} MB. ")

if __name__ == "__main__":
    main()