from bs4 import BeautifulSoup
import json


def checks(servers):
    with open('./html/index.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    '''Deze code opent de 'html' map en leest het 'index.html'-bestand in.'''
    report_div = soup.find('div', id='report_content')
    '''Deze code zoekt naar een `<div>`-element met de `id` "report_content".'''
    report_div.clear()
    '''Deze code zorgt ervoor dat de gevonden `<div>`-tag bij elke scan leeg is, 
    wat betekent dat de inhoud ervan wordt verwijderd of gewist.'''
    for server, is_up in servers.items():
        status = 'UP' if is_up else 'DOWN'
        div_tag= soup.new_tag('div',attrs={'class': 'server'})
        p_tag = soup.new_tag('p', attrs={'class': f'{status}'})
        div_tag.string=server
        report_div.append(div_tag)
        report_div.append(p_tag )
    '''Deze `for`-loop doorloopt de items één voor één en en kent hen een klassen toe, als ze 'up' of 'down' zijn op basis van hun status.
      Voor elke server/host wordt een `<div>`-element gemaakt met een `<p>`-tag erin. 
      De `<p>`-tag krijgt een klasse toegewezen die groen zal zijn als de status 'up' is en rood als de status 'down' is.'''
    with open('./html/index.html', 'w') as f:
        f.write(str(soup))



