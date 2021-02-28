import sys
from check_validity_of_ip_file import check_validity_of_ip_file
from check_validity_of_ip_addresses import check_validity_of_ip_addresses
from check_reachability_of_ip_addresses import check_reachability_of_ip_addresses
from establish_ssh_connection import establish_ssh_connection
from thread_module import thread_module

# Importing IP addresses
list_of_ip = check_validity_of_ip_file()

# Validity of IP addresses
try:
	check_validity_of_ip_addresses(list_of_ip)
except KeyboardInterrupt:
	print("\n Exiting....")
	sys.exit()

# Reachability of IP addresses
try:
	check_reachability_of_ip_addresses(list_of_ip)
except KeyboardInterrupt:
	print("\n Exiting....")
	sys.exit()

# SSH Connection
thread_module(list_of_ip, establish_ssh_connection)