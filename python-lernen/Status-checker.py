def check_status(wert):
    status = True
    if wert > 80:
        status = False
    return status

def main():

    systemlast = [45, 88, 20, 95]
    server = 1

    for auslastung in systemlast:
        if check_status(auslastung):
            print(f" Server {server} OK ")

        else:
            print(f" Server {server} überlastet! ")

    server += 1

if __name__ == "__main__":
    main()