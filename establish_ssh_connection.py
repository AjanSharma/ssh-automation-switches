# paramiko is used to perform ssh operations on the devices
import paramiko
import os.path
import time 
import sys
import re

# For establishing the ssh connection it becomes necessary to check the usernames and passwords file.
un_pass_file = input("\n Enter the path and the name of credential file: ")
if os.path.isfile(un_pass_file) == True:
	print("\n File is valid")
else:
	print("\n File {} does not exist ".format(un_pass_file))
	sys.exit()

# Next comes the commands file that contains commands that needd to be executed.
commands_file = input("\n Enter the path and name of the commands file: ")
if os.path.isfile(commands_file) == True:
	print("\n File is valid")
else:
	print("\n File {} does not exist ".format(commands_file))
	sys.exit()

# SSH Connection
def establish_ssh_connection(ip):
    
    global un_pass_file
    global commands_file
    
    # Creating SSH CONNECTION
    try:
        # Open Username and Password file
        credential_file = open(un_pass_file, 'r')
        
        # Reading from the beginning of the file
        credential_file.seek(0)
        
        # Usernames
        username = credential_file.readlines()[0].split(',')[0].rstrip("\n")
        
        # Reading from the beginning of the file
        credential_file.seek(0)
        
        # Passwords
        password = credential_file.readlines()[0].split(',')[1].rstrip("\n")
        
        # Logging into device using paramiko
        session = paramiko.SSHClient()
        
        # AutoAddPolicy() allows auto-accepting unknown host keys
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Using username and password to connect          
        session.connect(ip.rstrip("\n"), username = username, password = password)
        
        # Invoke Shell Session
        conn = session.invoke_shell()	
        
        # Disable pagination
        conn.send("enable\n")
        conn.send("terminal length 0\n")
        time.sleep(1)
        
        # Global config mode
        conn.send("\n")
        conn.send("configure terminal\n")
        time.sleep(1)
        
        # Opening Commands File
        cmd_file = open(commands_file, 'r')
            
        #Starting from the beginning of the file
        cmd_file.seek(0)
        
        #Writing each line in the file to the device
        for each_line in cmd_file.readlines():
            conn.send(each_line + '\n')
            time.sleep(2)
        
        #Closing the user file
        credential_file.close()
        
        #Closing the command file
        cmd_file.close()
        
        # Grabbing Output
        output = conn.recv(65535)
        
        if re.search(b"% Invalid input", output):
            print("IOS error occured {} :(".format(ip))
            
        else:
            print("\nOutput for {} \n".format(ip))
            
        #Test for reading command output
        #print(str(output) + "\n")
        o = output.decode('UTF-8')
        print(o + "\n")
        #fixed_output = o.split('\r\n')
        #print(fixed_output)
        #for i in fixed_output:
        #	print(i + "\n\n")
        
        #Closing the connection
        session.close()
     
    except paramiko.AuthenticationException:
        print("Invalid username or password")
        print("Closing program...")