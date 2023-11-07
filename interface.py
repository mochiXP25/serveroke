import sys
from rich import print
from managment import *
def interface():
    while True:
        print("Menu")
        print("-------------------")
        print("1.toevoegen van een server")
        print("2.verwijderen van een server")
        print("3.server lijst tonen")
        print("4.Stop het programma ")
        keuze=input("Maak je keuzen:  ")
        match keuze:
            case '1':
                server=input("voer de servernaam in: ")
                server_toevoegen(server)
            case '2':
                server=input("voer de servernaam in: ")
                server_verwijderen(server)
            case '3':
                print(laad_file())
            case '4':
                sys.exit()
            case _ :
              print("ongeldige keuzen")  
'''
Deze functie bevat een keuzemenu dat in een while loop blijft lopen. 
Het vraagt de gebruiker naar input en biedt 5 mogelijke antwoorden:

1. Server toe te voegen aan de lijst.
2. Server uit de lijst te verwijderen.
3. Print alle servers in de lijst naar het terminalvenster.
4. Stop de code zonder de noodzaak van CTRL+C.
5. De "default" of "case _" om ongeldige invoer van de gebruiker af te handelen en mogelijke crashes te voorkomen.'''
