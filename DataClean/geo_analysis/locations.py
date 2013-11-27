#!/usr/bin/env python
#coding: utf8 
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import cm


# import vector data


# available libraries
from osgeo import gdal
# for i in range(gdal.GetDriverCount()):
# 	print gdal.GetDriver(i).LongName

from collections import defaultdict


DIRECTORY = '/Users/mattstringer/Dropbox/ProyectoLaCumbre/DataClean/FincaNames/'
# os.chdir(DIRECTORY)
# text_files = [DIRECTORY + "/" + files for files in glob.glob("*.csv")]
# for i in text_files:





def main():

	points = dict()
	d = defaultdict(list)

	year_points = defaultdict(list)

	f = open('new_master_data.csv', 'r')
	opened_file = f.readlines()[1:]
	f.close()

	lats = []
	lons= []

	for i in opened_file:
		column=i.split("~")
		if len(column) == 30 and column[9] != '':
			finca_name = column[2]
			latitude = float(column[8])
			longitude = float(column[9])
			certification_year = column[17]



			points[finca_name] = [(latitude, longitude), certification_year]
			year_points[certification_year].append(latitude)
			d['lat'].append(latitude)
			d['lon'].append(longitude)
			d['cert_num'].append(certification_year)
			d['finca_name'].append(finca_name)

	for key, value in sorted(year_points.items()):
		print key, len(value)


	west, south, east, north = -90.1, 12.8, -87.70, 14.5
	
	fig = plt.figure(figsize=(11.7,8.3))
	#Custom adjust of the subplots
	plt.subplots_adjust(left=0.05,right=0.95,top=0.90,bottom=0.05,wspace=0.15,hspace=0.05)
	ax = plt.subplot(111)
	#Let's create a basemap around Belgium
	m = Basemap(resolution='i',projection='merc', llcrnrlat=south,urcrnrlat=north,llcrnrlon=west,urcrnrlon=east,lat_ts=51.0)
	m.drawcountries(linewidth=0.5)
	m.drawcoastlines(linewidth=0.5)
	 
	m.drawparallels(np.arange(south,north,1.),labels=[1,0,0,0],color='black',dashes=[1,0],labelstyle='+/-',linewidth=0.2) # draw parallels
	m.drawmeridians(np.arange(west,east,1.),labels=[0,0,0,1],color='black',dashes=[1,0],labelstyle='+/-',linewidth=0.2) # draw meridians
	


	lon = d['lon']

	lat = d['lat']

	x,y = m(lon, lat)
	m.plot(x, y, 'bo', markersize=8)
	plt.title("Coffee Fincas")
	plt.savefig('certified_locations.png', dpi=300, bbox_inches='tight')

	




	plt.show()


print "done."

if __name__ == '__main__':
    main()
    print "done."