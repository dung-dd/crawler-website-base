import socket
from config import *
s = socket.socket()
server = ('www.24h.com.vn', 80)
s.connect(server)

data_send = "GET / HTTP/1.1\r\nHost: www.24h.com.vn\r\nConnection: close\r\n\r\n"
data_recv = ''
s.send(data_send)
while 1:
	try:
		chunk = s.recv(1024)
		data_recv += chunk
	except socket.error:
		break
	if chunk == '':
		break
		
print data_recv
