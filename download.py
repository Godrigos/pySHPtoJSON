import ftplib
import os
from alive_progress import alive_bar


def dlzip(data='brasil'):
    """Download 2020 zip files from ftp://geoftp.ibge.gov.br."""

    mainUrl = 'geoftp.ibge.gov.br'
    urlDir = '/organizacao_do_territorio/malhas_territoriais/' \
        'malhas_municipais/municipio_2020/'

    if data.lower() == 'brasil' or 'brazil':
        level = 'Brasil/BR/'
    elif data.lower() == 'uf' or 'ufs':
        level = 'UFs/'
        uf = ''
    else:
        level = 'Brasil/BR/'

    try:
        ftp = ftplib.FTP(mainUrl)
        ftp.login()
        ftp.cwd(urlDir + level)

        files = ftp.nlst()

        if not os.path.isdir("zip"):
            os.mkdir('zip')
    except ftplib.all_errors:
        print("FTP connection error!")
        exit(1)

    with alive_bar(len(files), bar='blocks') as bar:
        for file in files:
            if os.path.exists('./zip/' + file):
                bar()
                pass
            else:
                ftp.retrbinary('RETR ' + file,
                               open('./zip/' + file, 'wb').write)
                bar()

    print()
    ftp.close()
