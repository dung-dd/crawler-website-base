"""
Date: 17/3/16
Author: BuiT.Dung
Main Handle. Call to others files in folder crawl

"""

from audit import Audit
from config import *
class Crawler(object):
	def __init__(self):
		self.service = None
		self.is_run = True
		self.clients = []
		self.create_socket(MAX_CLIENT)


	def crawl(self, conn, url):
		"""
			:argv: string argv[1] with host, port, module
		"""
		print str(conn.getsockname()) + "  find url: " + url
		results = Audit(conn, url)
		conn.close()
		self.clients.remove(conn)


	def create_socket(self, MAX_CLIENT):
		"""PORTS : 50000"""	
		server = (SERVER, PORT)
		self.service = socket.socket()
		self.service.bind(server)
		self.service.listen(MAX_CLIENT)
		while self.is_run:
			try:
				conn, addr = self.service.accept()
				if len(self.clients) < MAX_CLIENT:
					# print "thread 1 will start"
					url = conn.recv(100)
					url = url.replace(chr(10), '')
					if ("close" == url.lower()):
						self.is_run = False
						continue
					thread.start_new_thread(self.crawl, (conn, url, ))
					self.clients.append(conn)
				else:
					conn.close()
			except Exception, e:
				pass
		for _ in self.clients:
			_.close()
		self.service.close()


if __name__ == "__main__":
	import sys, socket
	import thread

	c = Crawler()
