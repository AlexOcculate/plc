import MySQLdb
import glob
import os
import codecs
import re

DROPBOX_PATH = "/Users/mattstringer/Dropbox/ProyectoLaCumbre/DataClean/exporters"


class Database:

	host="localhost"
	user="root"
	password="yourpassword"
	db="coffee"

	queryCount = 0

	def __init__(self):
		self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db, charset='utf8', use_unicode=True)
		self.cursor = self.connection.cursor()

	def insert(self, query, object=None):
		try:
			if object is None:
				self.cursor.execute(query)
			# elif isinstance(object, Tweet):
				# self.cursor.execute(query, (object.tweet_id, object.tweet, object.truncated, object.tweet_date, object.language, object.retweet, object.retweeted, object.retweet_count, object.x_coordinate, object.y_coordinate, object.favorited, object.favorite_count, object.twitter_id_fkey))

				
			Database.queryCount += 1
		except Exception as e:
			print sys.exc_info()
			self.connection.rollback()
			print "exception"

	def displayCount(self):
		Database.queryCount

	def __del__(self):
		self.connection.close()


class Company:

	def __init__(self, company, website, office_address, city, state, post_code, country, contact, contact_email, phone, fax, business_type, brands, distribution_range, company_description):
			self.company = company
			self.website = website
			self.office_address = office_address
			self.city = city
			self.state = state
			self.post_code = post_code
			self.country = country
			self.contact = contact
			self.contact_email = contact_email
			self.phone = phone
			self.fax = fax
			self.business_type = business_type
			self.brands = brands
			# self.distribution_range = distribution_range
			# self.company_description

class CleanData:
	def __init__(self):
		self.data_unclean = []


f1 = open(DROPBOX_PATH + "/" + '[semi-clean]Exporter.csv', 'w')
f1.write("Company" +"\t" + "website"  +"\t" + "office address" +"\t" + "city "+ "\t" + "state " + "\t" + "Post code" +"\t"+ "Country" 
	+ "\t" + "Contact" + "\t" + "contact email" + "\t" + "phone" + "\t" + "Fax"+ "\t" + "Business type" + "\t" + "Brands" + "\t" + "Distribution Range" 
	+ "\t" + "Company Description"+ "\n")





db = Database()
# drop_table = "DROP TABLE IF EXISTS companies"
# create_table = """CREATE TABLE IF NOT EXISTS companies(
# 					id INTEGER NOT NULL AUTO_INCREMENT,
# 					company_name VARCHAR(100),
# 					website VARCHAR(100),
# 					office_address VARCHAR(100),
# 					description TEXT COMMENT 'twitter users account description',
# 					created_date DATETIME COMMENT 'date account was created',
# 					location VARCHAR(100) COMMENT 'location given by twitter user',
# 					time_zone VARCHAR(100),
# 					num_followers INTEGER COMMENT 'number of followers that installer follower has',
# 					num_friends INTEGER COMMENT 'number of friends that installer follower has',
# 					num_tweets INTEGER COMMENT 'total number of tweets',
# 					installer_id_fkey INTEGER,
# 					PRIMARY KEY (id),
# 					FOREIGN KEY (installer_id_fkey) REFERENCES accounts(twitter_id))
# 						ENGINE = InnoDB;"""





os.chdir(DROPBOX_PATH)
text_files = [DROPBOX_PATH + "/" + files for files in glob.glob("*.txt")]


def open_data(filename):
	f = open(file_name, "r")
	opened_file = f.readlines()
	f.close()
	files.append(opened_file)
	return files

files = []


for file_name in text_files:
	open_data(file_name)

businesses = []
locations = []

for each in files:
	for i in each:
		line=i.split("\r")
		
		for j in range(len(line)):
			row = line[j]
			item = row.split('\t')


			website = ""
			if item[0] == "Company":
	 			company = item[1].strip()
			
	 			f1.write(company +"\t")
	 			if "Office Address" in line[j+1]:
	 				website = "no website found"
	 			else:
	 				website = line[j+1].replace('\t', "")

	 			f1.write(website.strip() +"\t") 
	 			
		
	 		elif item[0] == "Office Address":

	 			
	 	  
	 			address_list = item[1].split(",")
	 			address_stuff = ""

	 			if len(address_list) < 4 or len(address_list) > 6:
	 				f1.write("[address incomplete]" + item[1].replace('"', "") + "\t" + "\t" + "\t"  + "\t"+ "\t")

	 			elif len(address_list) == 4:
					address = address_list[0].replace('"', "").strip()
					city = address_list[1].strip()
					state = address_list[2].strip()
					country = address_list[3].strip()

					f1.write(address +"\t" + city +"\t" + state +"\t"+"\t" + country.replace('"', "") +"\t")


				elif len(address_list) == 5:
					address = address_list[0].replace('"', "").strip()
					city = address_list[1].strip()
					state = address_list[2].strip()
					post_code = address_list[3].strip()
					country = address_list[4].strip()

					f1.write(address +"\t" + city +"\t" + state +"\t" + post_code +"\t" + country.replace('"', "") +"\t")

				elif len(address_list) == 6:
					address = address_list[0].replace('"', "").strip() + " " + address_list[1].strip()
					city = address_list[2].strip()
					state = address_list[3].strip()
					post_code = address_list[4].strip()
					country = address_list[5].strip()

					f1.write(address +"\t" + city +"\t" + state +"\t" + post_code +"\t" + country.replace('"', "") +"\t")
				#f1.write(address_stuff)

	 		elif item[0] == "Primary Contact":
	 			primary_contact = item[1].replace('\t', "").strip()
	 			f1.write(primary_contact +"\t") 
	 			email = line[j+1].replace('\t', "").strip()
	 			f1.write(email +"\t") 


	 		elif item[0] == "Phone":
				phone = item[1]
				f1.write(phone +"\t")
				
			elif item[0] == "Fax":
				fax = item[1]
				f1.write(fax +"\t")



			elif item[0] == "Business Type":
				business_type = item[1]
				for i in business_type.split(","):
					remove = i.replace('"', "").replace(')', "").replace('(', "").strip()
					if remove not in businesses:
						businesses.append(remove)
				f1.write(business_type +"\t")
			

	 		elif item[0] == "Brands":
	 			brands = ""
	 			if len(item[1]) == 0:
	 				brands = "none"
	 			else:
	 				brands = item[1]
	 			
	 			f1.write(brands +"\t")

			elif item[0] == "Distribution Range":
				distribution_range = item[1]
				f1.write(distribution_range +"\n")
				locales = distribution_range.split(",")
				for i in locales:
					remove = i.replace('"', "").replace(')', "").replace('(', "").strip()
					if remove not in locations:
						locations.append(remove)


			# elif item[0] == "Company Description ":
			# 	company_description = item[1]
			# 	f1.write(company_description +"\n")


for i in locations:
	print i
f1.close()


