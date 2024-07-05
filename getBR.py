import requests
from bs4 import BeautifulSoup


def getBR(mainURL: str) -> list[str]:

    table = BeautifulSoup(requests.get(mainURL).text,
                          'html.parser').find('table')

    links: list[str] = []
    for tr in table.findAll('tr'):
        trs = tr.findAll('td')
        for each in trs:
            try:
                link = each.find('a')['href']
                links.append(link)
            except:
                pass

    return [f'{mainURL}/{link}' for link in links[1:]]
