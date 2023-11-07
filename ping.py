import subprocess
import platform
import json
from datetime import datetime

def ping():
    result = {}
    hosts_file='server.json'
    log_file='log.json'
    data=[]
    try:
        with open(hosts_file, "r") as f:
            servers = json.load(f)
    except FileNotFoundError or json.JSONDecodeError:
        return {}
    '''
Dit codeblok probeert het bestand 'server.json' te openen
in de leesmodus met een `try`-blok en slaat de inhoud op in een variabele. 
Het `except`-blok wordt gebruikt om mogelijke fouten af te handelen, 
zoals het geval waarin het bestand niet gevonden kan worden of niet correct functioneert.    '''
    try:
        with open(log_file, "r") as l:
            data = json.load(l)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    '''zelfde als hierboven, maar dit opent de log file'''
    for server in servers:
        parameter = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", parameter, '1', server]
        response = subprocess.call(command)
        result[server] = response == 0
        '''Deze `for`-loop begint met het bepalen van het besturingssysteem van de computer en slaat dit op in de variabele "parameter". 
        Vervolgens wordt voor elke host/IP in het "server.json"-bestand één keer een pingcommando uitgevoerd. 
        De uitvoer van het commando wordt opgeslagen in de variabele "commando", 
        en aan de hand van de respons wordt gecontroleerd of het pingen naar de host al dan niet succesvol was.
        '''
       
        log_entry = {
            "timestamp": datetime.now().strftime(" %H:%M:%S %Y/%m/%d"),
            "ping_success": result
        }
        '''
        Alle informatie wordt vervolgens opgeslagen in een dictionary met de naam "log_entry".
          De datum fungeert als de sleutel en de hostnamen met hun pingresultaten worden opgeslagen als waarden.
        '''

    data.append(log_entry)
    with open(log_file, "w") as l:
        json.dump(data,l,indent=4)
    '''Ten slotte wordt de dictionary "log_entry" weggeschreven naar het JSON-logbestand.'''
    return result
