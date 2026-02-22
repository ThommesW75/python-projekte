def passwort_check(pw):
    pruefung = True
    if len(pw) < 8:
        pruefung = False
    return pruefung

def main():

    while True:
        password = input("Bitte gebe ein Passwort ein (min 8 Zeichen):")
        check = passwort_check(password)
        if check:
            print("Passwort akzeptiert")
            break
        else:
            print("Passwort nicht akzeptiert")

    print("Willkommen im System")

if __name__ == "__main__":
    main()