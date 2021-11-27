#!/usr/bin/env python3

import geopandas as gpd
import os
from download import dlzip
from halo import Halo


def main():
    dlzip()

    if os.path.isdir("zip"):
        files = os.listdir('zip')

    if not os.path.isdir("geo"):
        os.mkdir('geo')

    spinner = Halo(spinner='dots', color='white')

    for file in files:
        spinner.start(text=f'\rConverting shapefile in {file} to GeoJSON.')
        shape = gpd.read_file('./zip/' + file)
        shape.to_file('./geo/' + os.path.splitext(file)
                      [0] + '.geojson', driver='GeoJSON')
        spinner.succeed()


if __name__ == '__main__':
    main()
