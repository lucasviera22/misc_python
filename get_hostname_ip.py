import socket
import sys
# https://docs.python.org/3/library/socket.html

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
address = socket.gethostbyaddr(ip)

print("Hostname: " + hostname)
print("IP: " + ip)
print(address)

#Scan ports
target = socket.gethostbyname(ip)

try:
    for port in range (1,1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print ("Port {} is open.".format(port))
        s.close()
except:
    print("End...")
    sys.exit(0)