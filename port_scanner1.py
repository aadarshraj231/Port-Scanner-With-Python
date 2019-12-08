
#!/usr/bin/python


string="Google Code In Port Scanner"
length=len(string)
for row in range(length):
    for col in range(row+1):
        print(string[col],end=" ")
    print()

print()


import socket

#sock is variable
#socket is module package for networking
#socket.AF_INET stand for ipv4 address
#socket.SOCK_STRAM stand for tcp packets
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#i also set timeout 
socket.setdefaulttimeout(2)

#creating a host variable for containing a ipv4 address
host=input("Enter the host to scan : ")
#In Port you give  port number
port=int(input("Enter the port to scan : "))

#In function port_scanner take only one argument and argument is port
def port_scanner(port):
	#sock.connect_ex means if host,port not connect or not open then that candition true and else this condition not true then this
        # else condition is execute and show open and close ports
	if sock.connect_ex((host,port)):
	    print("Port %d is closed"%(port))
	else:
	    print("Port %d is opened"%(port))

#calling function port_scanner(port)
port_scanner(port)
