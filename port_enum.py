import sys
import socket
from datetime import datetime 



if len(sys.argv) == 2
	target = socket.gethostbyname(sys.argv[1])
else:
	print ("Invalid amount of arguments")
	print ("Syntax: python3 <script.py> <ip> ")


print ( "-" * 50)
print ( "Scanning target" + target)
print ( "Time started" + str(datetime.now())
print ( "-" * 50 )




try:

			for port in range (num, num2):
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					socket.setdefaulttimeout(1)
					res = s.connect_ex((target, port)) 
					if res == 0:
							print (f"{port} is open")
					s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()
