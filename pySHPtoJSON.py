#!/usr/bin/env python3

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import geopandas as gpd
import os
from download import dlzip
from halo import Halo
import argparse
import topojson as tp


parser = argparse.ArgumentParser()
parser.add_argument('mesh', help='The mesh level to download and convert.',
                    type=str, choices=['Brasil', 'UFs'])
args = parser.parse_args()


def main():
    dlzip(args.mesh)

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
