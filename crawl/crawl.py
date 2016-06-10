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
		

	def start(self):
		self.create_socket(MAX_CLIENT)


	def debug(self, string):
		print string


	def crawl(self, conn, url):
		"""
			:argv: string argv[1] with host, port, module
		"""
		client = conn.getpeername()
		self.debug (YELLOW + str(client) + "  crawl url: " + url + WHITE)
		results = []
		A = Audit(conn, url)
		results = A.RESULTS
		conn.close()
		self.clients.remove(conn)
		self.debug (BLUE + "=" * 60 + WHITE)
		self.debug (BLUE + "||\t" + str(client) + "  disconnect" + "\t\t||" + WHITE)
		self.debug (BLUE + "||\t" + "Search: " + url + ", Results: " + str(len(results)) + "\t\t||" + WHITE)
		self.debug (BLUE + "=" * 60 + WHITE)
		exit()


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
					self.debug (AQUA + "Max Client" + str(server) + WHITE)
					conn.close()
			except KeyboardInterrupt:
				for _ in self.clients:
					self.debug (RED + "Closed connect with " + YELLOW + str(_.getpeername()) + WHITE)
					_.close()
				self.debug (BLUE + "Closed listen in " + str(server), WHITE)
				self.service.close()
				exit()

		for _ in self.clients:
			self.debug (RED + "Closed connect with " + YELLOW + str(_.getpeername()) + WHITE)
			_.close()
		self.debug (BLUE + "Closed listen in " + str((SERVER, PORT)) + WHITE)
		self.service.close()

if __name__ == "__main__":
	import sys, socket
	import thread
	print AQUA , "Listen in ", (SERVER, PORT), WHITE
	c = Crawler()
	c.start()
