import ftplib
import os
from alive_progress import alive_bar
from states import states
from time import sleep


def dlzip(data):
    """Download 2020 zip files from ftp://geoftp.ibge.gov.br."""

    mainUrl = 'geoftp.ibge.gov.br'
    urlDir = '/organizacao_do_territorio/malhas_territoriais/' \
        'malhas_municipais/municipio_2020/'
    files = []

    try:
        ftp = ftplib.FTP(mainUrl)
        ftp.login()

        if not os.path.isdir("zip"):
            os.mkdir('zip')
    except ftplib.all_errors:
        print("FTP connection error!")
        exit(1)

    if data == 'Brasil':
        level = 'Brasil/BR/'
        ftp.cwd(urlDir + level)
        files = ftp.nlst()
    elif data == 'UFs':
        level = 'UFs/'
        for state in states:
            ftp.cwd(urlDir + level + state + '/')
            files = files + ftp.nlst()
    else:
        exit(1)

    with alive_bar(len(files), bar='blocks') as bar:
        if level == 'Brasil/BR/':
            for file in files:
                if os.path.exists('./zip/' + file):
                    bar()
                else:
                    ftp.retrbinary('RETR ' + file,
                                   open('./zip/' + file, 'wb').write)
                    bar()
        elif level == 'UFs/':
            for state in states:
                ftp.cwd(urlDir + level + state + '/')
                files = ftp.nlst()
                for file in files:
                    ftp.cwd(urlDir + level + state + '/')
                    ftp.retrbinary('RETR ' + file,
                                   open('./zip/' + file, 'wb').write)
                    bar()

    print()
    ftp.close()
