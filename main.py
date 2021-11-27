#!/usr/bin/env python3

import geopandas as gpd
import os
import io
from download import dlzip


def main():
    dlzip()

    if os.path.isdir("zip"):
        files = os.listdir('zip')

    for file in files:
        shape = gpd.read_file('./zip/' + file)
        shape.to_file(file + '.geojson', driver='GeoJSON')


if __name__ == '__main__':
    main()
