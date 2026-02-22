def finde_user(user_liste, gesuchter_name):
    for benutzer in user_liste:
        if benutzer == gesuchter_name:
            return True

    return False

def main():

    user = ["Thomas", "Tina", "Luki", "Lenni"]
    name = input("Welchen User suchst du? ")

    pruefung = finde_user(user, name)

    if pruefung:
        print(f" {name} ist vorhanden.")
    else:
        print(f" {name} ist nicht vorhanden.")

if __name__ == "__main__":
    main()