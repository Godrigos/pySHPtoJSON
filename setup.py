from cx_Freeze import setup, Executable
import os
import sys

executables = [Executable('pySHPtoJSON.py')]

BUILD_EXE_OPTIONS = {
    'build_exe': r'bin',
    'excludes': ['matplotlib', 'sqlite3', 'scipy', 'tkinter',
                 'PyQt4', 'PyQt5'],
    'path': [os.path.abspath('pySHPtoJSON')] + sys.path,
    'packages': ['numpy'],
    'includes': 'numpy',
}

setup(
    name='pySHPtoJSON',
    version='1.1',
    description='A CLI tool to download and convert shapefiles of Brazilian'
    ' territory made available by IBGE.',
    options={'build_exe': BUILD_EXE_OPTIONS},
    executables=executables,
)
