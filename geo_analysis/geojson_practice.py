#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import csv
import numpy as np
import geojson
from matplotlib.patches import Polygon
from shapely.geometry import shape, Point, MultiPoint
import matplotlib.pyplot as plt
# import fiona
import mpl_toolkits.basemap.pyproj as pyproj # Import the pyproj module
from random import randint
from collections import defaultdict


class data(object):

    def __init__(self,data_file):

        self.finca_id, self.latitude, self.longitude, self.certification_year = [], [], [], []

        for row in data_file:
        	try:
	            self.finca_id.append(row[2])
	            self.latitude.append(float(row[8]))
	            self.longitude.append(float(row[9]))
	            self.certification_year.append(int(row[17]))
	        
	        except ValueError as v:
	        	print "exception1", v, row[2]

	        except IndexError as i:
				print "IndexError1", i, row[2]

    def clean(self):
    	pass
        





fig = plt.figure()
fig.add_subplot(111, aspect='equal')
ax = fig.gca()



def plot_polygon(ax, poly, color='red'):
    a = np.asarray(poly.exterior)
    ax.add_patch(Polygon(a, facecolor=color, alpha=0.3))
    ax.plot(a[:, 0], a[:, 1], color='black')

def plot_multipolygon(ax, geom, color='red'):
    """ Can safely call with either Polygon or Multipolygon geometry
    """
    if geom.type == 'Polygon':
        plot_polygon(ax, geom, color)
    elif geom.type == 'MultiPolygon':
        for poly in geom.geoms:
            plot_polygon(ax, poly, color)




cwd = os.path.dirname(os.path.abspath(__file__))
dataDir = os.path.join(os.path.split(cwd)[0], 'Data')


'''
Data Files 
'''
#shapefiles
shpDir = os.path.join(dataDir, 'shapefiles')
shpfile = os.path.join(shpDir, u'SLV_adm1.shp')

# geoJSON
jsonDir = os.path.join(dataDir, 'geoJsonFiles')
jsonfile = os.path.join(jsonDir, 'ES_department_boundaries.json')
outer_bound = os.path.join(jsonDir, 'ES_country_boundary.json')

# finca data
fincaDir =  os.path.join(dataDir, 'finca_data')
finca_data = os.path.join(fincaDir, u'new_master_data.csv')




'''
use data
'''

es = geojson.load(open(outer_bound))
# print shape(es_outer_boundary)
es_outer_boundary = shape(es['features'][0]['geometry'])




es_open = geojson.load(open(jsonfile))


# need 14 colors
colors = ['#c3d4e4', '#618ab6', '#ccdda6', '#78a651', '#dfaeab', '#ba4942', '#eacf9d', '#d9964d','blue', '#ccc1dc', '#c1d4e8', '#ebd85e', '#52b581', 'yellow']



for i in range(len(es_open["features"])):
	el_salvador = shape(es_open["features"][i]['geometry'])

	color = colors.pop()
	plot_multipolygon(ax, el_salvador, color)






# es_ext = np.asarray(el_salvador.exterior)

west, south, east, north = el_salvador.bounds




tot_points = defaultdict(list)
points = {}

locations = defaultdict(list)

f = open(finca_data, 'r')
opened_file = f.readlines()[1:]
f.close()




for i in opened_file:
	column=i.split("~")

	# if len(column) == 30 and column[9] != '' and column[17] != '':

	finca_name = ''

	try:
		cert_num = column[1]

		finca = column[5]
		beneficio = column[6]


		finca_name = column[4]
		latitude = float(column[28])
		longitude = float(column[29])

		cultivated_area = float(column[32])
		tot_production = float(column[33])

		land_efficiency = tot_production / cultivated_area


		certification_year = float(column[17])

		pos_supply_chain = column[27]

		municipality = column[23]
		department = column[24]



		# if finca == beneficio:
		# 	print "true"

	
		tot_points['lat'].append(latitude)
		tot_points['lon'].append(longitude)
		tot_points['cultivated_area'].append(cultivated_area)
		tot_points['tot_production'].append(tot_production)
		tot_points['land_eff'].append(land_efficiency)



		tot_points['coor'].append((latitude,longitude))



		locations[department].append(finca_name)


		if certification_year not in points:
			points[certification_year] = {'lat': [], 'lon': [], 'finca': []}
			points[certification_year]['lat'].append(latitude)
			points[certification_year]['lon'].append(longitude)
			points[certification_year]['finca'].append(finca_name)
		else:
			points[certification_year]['lat'].append(latitude)
			points[certification_year]['lon'].append(longitude)
			points[certification_year]['finca'].append(finca_name)

		points[certification_year]['tot_count'] = len(points[certification_year]['lat'])

	
	except ValueError as v:
		print cert_num

	except IndexError as i:
		print "IndexError1", i, cert_num

def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]









locations = [(x[1], x[0]) for x in tot_points['coor']]

lon, lat = zip(*locations)

points = MultiPoint(zip(lon,lat))






points = MultiPoint([p for p in points.geoms if es_outer_boundary.contains(p)])
pt_arr = np.asarray(points)

value = 'cultivated_area'

median = median(tot_points[value])

values = zip(pt_arr, tot_points[value])



for i in values:
	if i[1] > median:
		color = "#0000FF"
	else:
		color = "#FF0000"

	
	plt.plot(i[0][0], i[0][1], marker='o', color = color, markersize=4, linestyle='None')


	# else:
	# 	plt.plot(i[0], i[1], marker='o', color = '#eeefff', markersize=2, linestyle='None')





plt.show()
# 	