# Brazil Atlas

Inspired by [Carolina Bigonha's br-atlas](https://github.com/carolinabigonha/br-atlas), this repository is for generating [TopoJSON](https://github.com/mbostock/topojson) and [GeoJSON](https://geojson.org) files for Brazilian maps.

All maps are downloaded from [IBGE (Instituto Brasileiro de Geografia e Estatística)](http://www.ibge.gov.br/), the agency responsible for
statistical, geographic, cartographic, geodetic and environmental information
in Brazil and were published on 2021.

## Dependencies

Firstly, this repository depends on [Python 3](https://www.python.org/).
You may install Python using the source code or a pre-built
installer for your platform, all available at
[Python download page](https://www.python.org/downloads/).

You also need [GDAL](https://gdal.org/) to be installed on you OS and available in your PATH.

The other dependencies are listed in the requirements.txt file and can be installed with `pip install -r requirements.txt`.

## Usage

Clone this repository, install the dependencies and run `./pySHPtoJSON.py -h` to read the instructions. Make sure that `pySHPtoJSON.py` file has execution permission.

TopoJSON files will be generated inside `topo/` directory.
GeoJSON files will be generated inside `geo/` directory.

## More Information

Running `./pySHPtoJSON.py Brasil` will generate TopoJSON and GeoJSON files for
Brazil and  `./pySHPtoJSON.py UFs` for each of its states, municipalities, macro and microregions. They are located in `BR/` and `UFs/` subdirectories.

Also, several original compacted shapefiles files are stored: `zip` directory contains these files downloaded from IBGE. If you wish you may delete this extra directory after conversion.

## Binaries
Binary executables may be generated for each platform by running `python3 setup.py build`. It will work only on the operational system that generated it.

This command will create a subdirectory called `bin` with the executable and its needed libraries at  a `lib` directory.
