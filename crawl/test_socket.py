import socket, thread, re, time

server = ('localhost', 50001)

s = socket.socket()
s.bind(server)
s.listen(3)
print "listen in {0}".format(server)
Num = 0
C = []

def func(c, num):
	time.sleep(3)
	c.send("Start new thread\n")
	data = str(dir(c))
	c.send(data + "\n")
	data = c.recv(100)
	print data 
	if re.match(data, "close"):
		c.close()
		print "Client %d closed\n" % num
	print "notmatch %d" % num
	print "%d before exit " % num
	exit()
	print "%d after exit " % num
	print "%d after exit " % num
	print "%d after exit " % num

while 1:
	try:
		
		conn, addr = s.accept()
		if Num < 5 :
			# conn.send(addr)
			conn.send("Hello {0}\n".format(Num+1))
			C .append(conn)
			Num += 1
			print "{0} Client connected\n".format(Num)
			x = thread.start_new_thread(func, (conn, Num,))
			print "Value of func {0}: {1}".format(Num,x)
		else:
			conn.close()
			break
	# for _ in C:
	# 	_.send("Close")
	# 	_.close()
	# s.close()
	# exit()

	except Exception, e:
		print e
		s.close()
		exit()
print "EXIT"