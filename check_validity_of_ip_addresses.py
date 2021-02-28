# This file take the Loopback, multicast, broadcast, link-local addresses.
import sys

# This method will check the validity of the IP addresses
def check_validity_of_ip_addresses(list_of_ip):
	
	for ip in list_of_ip:
		ip = ip.rstrip("\n")
		list_of_four_octets_in_ip = ip.split('.')

		if (len(list_of_four_octets_in_ip) == 4) and (1 <= int(list_of_four_octets_in_ip[0]) <= 223) and (int(list_of_four_octets_in_ip[0]) != 127) and (int(list_of_four_octets_in_ip[0]) != 169 or int(list_of_four_octets_in_ip[1]) != 254) and (0 <= int(list_of_four_octets_in_ip[1]) <= 255 and 0 <= int(list_of_four_octets_in_ip[2]) <= 255 and 0 <= int(list_of_four_octets_in_ip[3]) <= 255):
			continue
		else:
			print("\n Invalid IP address found - {}".format(ip))