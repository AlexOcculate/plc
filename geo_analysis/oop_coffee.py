points = {}


class Mapping:
	def __init__(self, data_csv):
		self.data_csv 			= data_csv
		self.finca_name 		= self.data_csv[2]
		self.latitude			= self.data_csv[8]
		self.longitude			= self.data_csv[9]
		self.certification_year	= self.data_csv[17]
		self. points = {}

		if self.certification_year not in self.points:
			self.points[self.certification_year] = {'lat': [], 'lon': [], 'finca': []}
			self.points[self.certification_year]['lat'].append(self.latitude)
			self.points[self.certification_year]['lon'].append(self.longitude)
			self.points[self.certification_year]['finca'].append(self.finca_name)
		else:
			self.points[self.certification_year]['lat'].append(self.latitude)
			self.points[self.certification_year]['lon'].append(self.longitude)
			self.points[self.certification_year]['finca'].append(self.finca_name)

		self.points[self.certification_year]['tot_count'] = len(self.points[self.certification_year]['lat'])









def main():
	PATH = '/Users/mattstringer/Dropbox/ProyectoLaCumbre/coffee_project/CertificationData/new_master_data2.csv'


	f = open(PATH, 'r')
	opened_file = f.readlines()[1:]
	f.close()

	for i in opened_file:
		column = i.split("~")
		if len(column) == 30 and column[9] != '':
			m = Mapping(column)

			print m.points






if __name__ == '__main__':
    main()
    print "done."	