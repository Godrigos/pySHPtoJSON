#!/usr/bin/env python3

import topojson as tp
import argparse
from halo import Halo
from download import dlzip
import os
import geopandas as gpd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


parser = argparse.ArgumentParser()
parser.add_argument('mesh', help='The mesh level to download and convert.',
                    type=str, choices=['Brasil', 'UFs'])
parser.add_argument('--year',
                    help='The year of the data to download. Defaults to 2022',
                    type=str, default='2022')
args = parser.parse_args()


def main():
    dlzip(args.mesh, args.year)

    if os.path.isdir("zip"):
        files = os.listdir('zip')

    print('##### GeoJSON #####')
    spinner = Halo(spinner='dots', color='white')

    for file in files:
        spinner.start(text=f'\rConverting shapefile in {file} to GeoJSON.')
        shape = gpd.read_file('./zip/' + file)
        if args.mesh == 'Brasil':
            if not os.path.isdir("geo/BR"):
                os.makedirs('geo/BR')
            shape.to_file('./geo/BR/' + os.path.splitext(file)
                          [0] + '.geojson', driver='GeoJSON')
        elif args.mesh == 'UFs':
            if not os.path.isdir("geo/UFs"):
                os.makedirs('geo/UFs')
            shape.to_file('./geo/UFs/' + os.path.splitext(file)
                          [0] + '.geojson', driver='GeoJSON')

        spinner.succeed()

    print('\n##### TopoJSON #####')

    for file in files:
        spinner.start(text=f'\rConverting shapefile in {file} to TopoJSON.')
        shape = gpd.read_file('./zip/' + file)
        if args.mesh == 'Brasil':
            if not os.path.isdir("topo/BR"):
                os.makedirs('topo/BR')
            tp.Topology(shape).to_json(fp='./topo/BR/' +
                                       os.path.splitext(file)[0] + '.json')
        elif args.mesh == 'UFs':
            if not os.path.isdir("topo/UFs"):
                os.makedirs('topo/UFs')
            tp.Topology(shape).to_json(fp='./topo/UFs/' +
                                       os.path.splitext(file)[0] + '.json')

        spinner.succeed()


if __name__ == '__main__':
    main()
