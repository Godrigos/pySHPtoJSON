from cx_Freeze import setup, Executable

executables = [Executable('pySHPtoJSON.py')]

setup(
    name='pySHPtoGeoJ',
    version='1.0',
    description='A CLI tool to download and convert shapefiles of Brazilian'
    ' territory made available by IBGE.',
    executables=executables,
)
