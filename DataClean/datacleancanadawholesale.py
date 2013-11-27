import sys

f=open("usa_retailers.txt","r")
usa=f.readlines()
f.close()

f=open("canada_retailers.txt","r")
canada=f.readlines()
f.close()

f=open("germany_retailers.txt","r")
germany=f.readlines()
f.close()

retailers = [usa, canada, germany]
print len(retailers)

f1 = open('[semi-clean]RoastersContactSpreadsheet.csv', 'w')
f1.write("Company" +"\t" + "website"  +"\t" + "office address" +"\t" + "city "+ "\t" + "state " + "\t" + "Post code" +"\t"+ "Country" 
	+ "\t" + "Contact" + "\t" + "contact email" + "\t" + "phone" + "\t" + "Fax"+ "\t" + "Business type" + "\t" + "Brands" + "\t" + "Distribution Range" 
	+ "\t" + "Company Description"+ "\n")


for each in retailers:
	for i in each:

		line=i.split("\r")

		for j in range(len(line)):
			row = line[j]
			item = row.split('\t')



			website = ""
			if item[0] == "Company":
	 			company = item[1].strip().strip()
	 			f1.write(company +"\t")
	 			if "Office Address" in line[j+1]:
	 				website = "no website found"
	 			else:
	 				website = line[j+1].replace('\t', "")

	 			f1.write(website.strip() +"\t") 
	 			
		
	 		elif item[0] == "Office Address":

	 			
	 	  
	 			address_list = item[1].split(",")
	 			address_stuff = ""

	 			if len(address_list) < 5 or len(address_list) > 6:
	 				f1.write("[address incomplete]" + item[1].replace('"', "") + "\t" + "\t" + "\t"  + "\t"+ "\t")



				if len(address_list) == 5:
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
				f1.write(distribution_range +"\t")

			elif item[0] == "Company Description ":
				company_description = item[1]
				print company_description
				f1.write(company_description +"\n")



f1.close()

