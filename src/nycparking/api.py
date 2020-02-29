from sodapy import Socrata

def get_violation(app_key,page_size:int,num_pages:int):
	#I tried the /resource and have the http:// in the beginning but does not work?
	API =Socrata("data.cityofnewyork.us", app_key)

	result =[]
	for i in range(0,num_pages):
		result.append(API.get('nc67-uf89',limit = page_size, offset = i*(page_size)))


	return result