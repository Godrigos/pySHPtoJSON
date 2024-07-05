import requests
from bs4 import BeautifulSoup
from consts import STATES


def getUFs(mainURL: str) -> list[str]:

    links: list[str] = []
    for state in STATES:
        table = BeautifulSoup(requests.get(f'{mainURL}/{state}').text,
                              'html.parser').find('table')
        for tr in table.findAll('tr'):
            trs = tr.findAll('td')
            for each in trs:
                try:
                    link = each.find('a')['href']
                    links.append(f'{state}/{link}')
                except:
                    pass

    return [f'{mainURL}/{link}' for link in links[1:]]
