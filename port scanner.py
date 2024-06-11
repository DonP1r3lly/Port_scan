import socket

target='localhost'
port=80
#create a socket object
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#set a timeout
s.settimeout(5)

def port_scanner(port):
    if s.connect_ex((target,port)):
        print("The port is closed")
    else:
        print("The port is open")

#Scan the firts 1024 ports
for port in range(0,1025):
    print(port)
    port_scanner(port)

port_scanner(port)