import config
# from get_link import *
import get_link

import socket
from URL import URL 
import re

crlf = "\r\n"
crlf_crlf = "\r\n\r\n"

DATA_SEND = "GET {0} HTTP/1.1\r\nHOST: {1}\r\nAgent: {2}\r\nConnection: close\r\n\r\n"
"""
data for request:

GET / HTTP1.1\r\n
HOST: crawler.com\r\n\r\n
Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0

"""

class Audit():
	"""
	"""
	def __init__(self, conn, url):
		self.conn = conn
		self.error = 0
		url = URL(url)
		self.QUEUES = [url]
		self.domain = url.domain
		self.port = url.port
		self.RESULTS = []
		self.audit(self.domain, url.port)
		self.conn.close()
		self.debug("-"*20+" END "+"-"*20)
		# self.test(url)


	def test(self, url):
		print dir(url)
		print "domain: ", url.domain
		print "port: ", url.port
		print "module: ", url.module
		print "folder: ", url.folder
		print "file_name: ", url.file_name
		print "params: ", url.params
		print "frames: ", url.frames


	def get_link(self, response, domain, port, folder):
		"""
			MAIN function handle crawler
		"""
		# find link in tags: a, link, form, button
		# call to all function in file get_link
		# for method in get_link:
		for attr in dir(get_link):
			item = getattr(get_link, attr)
			if callable(item) : # and attr=="get_link_tag_a"
				links = item(response, domain, port, folder)
				if isinstance(links, list):
					# del None element
					links = filter(None, links)			
					return links
		return []


	def audit(self, origin, response):
		"""
			:origin: original url.
			all url need match with original url
			:return: list url obj
		"""
		while len(self.QUEUES) > 0:
			url_ = self.QUEUES.pop()
			self.debug("Crawling URL: " + url_.get_url())  # print debug
			self.RESULTS.append(url_)
			header, response = self.connect_getdata(url_.domain, url_.port, url_.get_module())
			links = self.get_link(response, self.domain, self.port, url_.folder)
			for link in links:
				url = URL(link)
				if not self.is_in_results(url):
					if not self.is_in_queues(url):
						self.QUEUES.insert(0, url)
						self.debug(url.get_url())
						self.debug_socket(url.get_url())
			self.RESULTS = filter(None, self.RESULTS)


	def connect_getdata(self, host=None, port=None, module=None):
		"""	
			:module: path to file enviroment in server
			:return header, response 
		"""
		if host==None:
			host = self.domain
		if port==None:
			port = self.port
		if module==None:
			module = self.module

		s = socket.socket()
		s.settimeout(config.TIMEOUT)
		try:
			s.connect((host, port))
		except :
			return "",""
		# same:
		# GET / HTTP1.1
		# HOST: crawler.com
		# data_send = "GET {0} HTTP1.1\r\nHOST: {1}".format(module, host)
		data_send = DATA_SEND.format(module, host, config.AGENT)
		s.send(data_send)
		data_recv = ''
		while 1:
			try:
				chunk = s.recv(1024)
				data_recv += chunk
				# print chunk
			except socket.error:
				break
			if chunk == '':
				break
		header, body = "",""
		if crlf_crlf in data_recv:
			data = data_recv.split(crlf_crlf)
			header = data[0]
			body = "".join(_ for _ in data[1:])
		tmp__ = "1" if crlf_crlf in data_recv else "0"
		f = open("test.txt","a")
		f.write("----------------- "+module+"  "+tmp__+" ---------------------")
		f.write(data_recv)
		f.close()
		return header, body


	def is_in_queues(self, url):
		for _ in self.QUEUES:
			if url.get_url() == _.get_url():
				return True
		return False


	def is_in_results(self, url):
		if len(self.RESULTS):
			for _ in self.RESULTS:
				if url.get_url() == _.get_url():
					return True
		else:
			return False


	def append_QUEUES(self, links=[]):
		"""
			:links: is a list
			:check link in links if not in QUEUES, handle add to QUEUES with index 0
		"""
		for link in links:
			if not is_in_queues(link):
				self.QUEUES.insert(0, link)


	def debug(self, string):
		print string


	def debug_socket(self, string):
		"""
			:socket: a socket send :string to cmd
		"""
		try:
			self.conn.send(string + "\n")
		except:
			self.error = 1
			exit()