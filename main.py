import sys
from managment import *
from ping import ping
from checks import checks
from interface import interface
from server import run
server_file = "server.json"
servers = []

def main():
    if len(sys.argv) > 2 and sys.argv[1] == "management":
        if sys.argv[2] == "toevoegen" and len(sys.argv) > 3:
            print(server_toevoegen(sys.argv[3]))
        elif sys.argv[2] == "verwijderen" and len(sys.argv) > 3:
            print(server_verwijderen(sys.argv[3]))
        elif sys.argv[2] == "list":
            print(laad_file())
        else:
            print("Ongeldige keuze voor management.")
    elif len(sys.argv) > 1 and sys.argv[1] == "check":
        checks(ping())
        run()
    else:
        interface()

if __name__ == "__main__":
    main()
