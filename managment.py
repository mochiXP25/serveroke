import json
def laad_file():
    servers={}
    try: 
        with open('server.json', "r") as f:
            servers = json.load(f)
            return servers
    except FileNotFoundError:
        return []
'''Deze functie zal proberen een JSON-bestand te laden in de leesmodus, 
en als het bestand niet bestaat, zal het de fout afhandelen.'''

def opslaan(wijziging,):
    with open('server.json', "w") as f:
        json.dump(wijziging, f, indent=2)
'''Deze functie zal gegevens naar een JSON-bestand schrijven.'''

def server_toevoegen(item):
    data = laad_file()
    if item not in data:
        data.append(item)
        opslaan(data)
        return f"Server {item} werd toegevoegd."
    else:
        return f"Server {item} is al toegevoegd."
'''Deze functie zal een server in een JSON-bestand schrijven en 
eerst controleren of de server al dan niet al in het bestand staat.'''

def server_verwijderen(item):
    data = laad_file()
    if item in data:
        data.remove(item)
        opslaan(data)
        return f"Server {item} werd verwijderd."
    else:
        return f"Server {item} is niet teruggevonden in de lijst."
'''
Deze functie verwijdert een opgegeven server uit het 
JSON-bestand en roept vervolgens de laad_file functie aan om de wijzigingen op te slaan.'''
