import sys
import subprocess

# This method will check the reachability of the IP addresses
def check_reachability_of_ip_addresses(list_of_ip):
	for ip in list_of_ip:
		ip = ip.rstrip("\n")

		# Command = ping
		# %s = string operator
		# /n 2 = Number of echo request sent to each device.
		# ip = ip address to ping
		# DEVNULL = Because of DEVNULL the errors related to the ping command do not interfere.
		reply_got_from_ping = subprocess.call('ping %s /n 2' % (ip), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)

		# If the above command echo 0 it means ping is successfull
		if reply_got_from_ping == 0:
			print("\n {} is reachable :)\n".format(ip))
			continue
		else:
			print('\n* {} not reachable. Check connectivity and try again.'.format(ip))
			sys.exit()