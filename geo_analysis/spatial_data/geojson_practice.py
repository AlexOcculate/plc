import os

import geojson
from shapely.geometry import asShape
import fiona


cwd = os.path.dirname(os.path.abspath(__file__))

shpDir = os.path.join(os.path.split(cwd)[0])
print shpDir
# shpfile = os.path.join(shpDir, 'SLV_adm1.shp')
shpfile = cwd + '/shapefiles/SLV_adm1.shp'
print shpfile


es_geom = {}

with fiona.open(shpfile) as f:
	crs = f.crs
	