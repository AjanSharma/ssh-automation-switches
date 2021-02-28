import os.path
import sys

# Validity of the content as well as if the file is present or not
def check_validity_of_ip_file():

	#User Input
	file_input_by_user = input("\n Enter the path and the name of IP file: ")

	# Existence of file
	if os.path.isfile(file_input_by_user) == True:
		print("\n Processing the valid file")
	else:
		print("\n File {} does not exist".format(file_input_by_user))
		sys.exit()

	# Opening file for reading
	valid_ip_file = open(file_input_by_user, 'r')
	# Placing cursor at the beginning of the file
	valid_ip_file.seek(0)

	# Parsing each line of the file
	list_of_ip_addresses = valid_ip_file.readlines()

	valid_ip_file.close()

	return list_of_ip_addresses