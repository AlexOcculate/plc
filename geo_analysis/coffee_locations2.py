import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



def line_graph(x, x_title, y, y_title):
	plt.plot(x, y)
	plt.ylabel(y_title)
	plt.xlabel(x_title)
	plt.savefig('certification_timeseries.png', dpi=300, bbox_inches='tight')
	plt.show()






def main():
	west, south, east, north = -90.1, 12.8, -87.70, 14.5
	DIRECTORY = '/Users/mattstringer/Dropbox/ProyectoLaCumbre/DataClean/FincaNames/'

	PATH = '/Users/mattstringer/Dropbox/ProyectoLaCumbre/coffee_project/CertificationData/new_master_data2.csv'
	points = dict()
	f = open(PATH, 'r')
	opened_file = f.readlines()[1:]

	f.close()

	lats = []
	lons= []



	for i in opened_file:
		column=i.split("~")



		if len(column) == 30 and column[9] != '' and column[17] != '':
			finca_name = column[2]
			latitude = float(column[8])
			longitude = float(column[9])
			certification_year = float(column[17])




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

	tot_count = []
	year = []
	for key, value in sorted(points.items()):
		tot_count.append(value['tot_count'])
		year.append(key)

	

	line_graph(year, "Year", tot_count, "Count Certified")
if __name__ == '__main__':
    main()


# for year in sorted(points.keys()):
# 	print year, points[year]['tot_count']



# # definitions for the axes
# left, width = 0.07, 0.65
# bottom, height = 0.1, .8
# bottom_h = left_h = left+width+0.02

# rect_cones = [left, bottom, width, height]
# rect_box = [left_h, bottom, 0.17, height]

# fig, axes = plt.subplots(nrows=6, ncols=2)

# for i, ax in enumerate(axes.flat):
# 	items = sorted(points.items())[i]
# 	year = items[0]
# 	print year
# 	lat = items[1]['lat']
# 	lon = items[1]['lon']


# 	m = Basemap(resolution='i',projection='merc', llcrnrlat=south,urcrnrlat=north,llcrnrlon=west,urcrnrlon=east,lat_ts=51.0,ax=ax)
# 	m.drawcountries(linewidth=0.5)
# 	m.drawcoastlines(linewidth=0.5)
# 	ax.set_title(year)

# 	# lon = points['2008']['lon']
# 	# lat = points['2008']['lat']

# 	x,y = m(lon, lat)
# 	m.plot(x, y, 'bo', markersize=4)

# plt.savefig('certified_locations.png', dpi=300, bbox_inches='tight')
# plt.show()