class Server:

    def __init__(self, name):

        self.name = name

    def ausgabe(self):

        print(f" {self.name} eingerichtet")

def main():

    mein_server = Server("Webserver")

    print(f"Typ von mein_server: {type(mein_server)}")

    mein_server.ausgabe()

if __name__ == '__main__':
    main()


