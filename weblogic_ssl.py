import sys
import ssl
import socket

server_address = sys.argv[1]
port = int(sys.argv[2])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)
wrappedSocket = ssl.wrap_socket(sock)
wrappedSocket.connect((server_address,port))
# Send headers
headers = 't3 12.2.1\nAS:255\nHL:19\nMS:10000000\nPU:t3://test:7001\n\n'
wrappedSocket.sendall(headers)

try:
        data = wrappedSocket.recv(1024)
        print data
except socket.timeout:

       sock.close()
if "HELO" in data:
        print " - Vulnerable Weblogic: "+server_address+" ("+str(port)+")"
