import os
import sys
from alive_progress import alive_bar
from getBR import getBR
from getUFs import getUFs
from urllib.request import urlretrieve, urlopen


def dlzip(data: str, year: str):
    """Download 2022 zip files from ftp://geoftp.ibge.gov.br."""

    mainURL: str = 'https://geoftp.ibge.gov.br' \
        '/organizacao_do_territorio/malhas_territoriais' \
        f'/malhas_municipais/municipio_{str(year)}/'

    try:
        urlopen(mainURL)
    except Exception as e:
        sys.exit(e)

    links: list[str] = []

    if not os.path.isdir("zip"):
        os.mkdir('zip')

    if data == 'Brasil':
        links = getBR(f'{mainURL}Brasil/BR/')
    elif data == 'UFs':
        links = getUFs(f'{mainURL}UFs')
    else:
        exit(1)

    with alive_bar(len(links), bar='blocks') as bar:
        if data == 'Brasil':
            for link in links:
                if os.path.exists(f'./zip/{os.path.basename(link)}'):
                    bar()
                else:
                    urlretrieve(link, f'./zip/{os.path.basename(link)}')
                    bar()
        elif data == 'UFs':
            for link in links:
                if os.path.exists(f'./zip/{os.path.basename(link)}'):
                    bar()
                else:
                    urlretrieve(link, f'./zip/{os.path.basename(link)}')
                    bar()
    print()
