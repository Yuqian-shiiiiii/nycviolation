import sys
import os

from src.nycparking.api import get_violation

if __name__=="__main__":
	
	#only count the ones after first variable
	args = sys.argv[1:]
	print(args)

	#arg shows all the variables. the first variable arg[0] is the app key and so on
	app_key = os.getenv(f'APP_KEY')
	print(app_key)

	page_size = int(args[0])
	num_pages = int(args[1])
	output = args[2]

	violation = get_violation(app_key,page_size,num_pages)
	print(violation)
	with open(output,'w') as output_file:
		for lines in violation:
			for line in lines:
				output_file.write(f"{line}"+'\n')