import re

class URL():
	"""URL object has 3 abtribute
		:full_url: string
		:param: list
		:extension: string : extension for url
	"""
	def __init__(self, url=None):
		self.url = url
		self.domain = ''
		self.port = None # int
		self.file_name = ''
		self.extension = ''
		self.frames = ''
		self.params = []
		self.extension = "" # exame: php, html, aspx, etc
		self.folder = "" # exame: /, /folder1/folders, ...
		self.module = "" # module = folder + filename (full_path_to_file)
		if self.url:
			self.detach(url)
			self.set_module()


	def set_module(self):
		self.module = self.folder+"/"+self.file_name


	def get_module(self):
		return self.module


	def detach(self, uri):
		"""
			detach host, port, folder, file_name, extension, params, frames
			:return: host, port, module, folder, file_name, extension
			All methods will call to this function to get value
			priority: uri > self.url
		"""
		domain = ''
		port = 80
		folder = ''
		file_name = ''
		extension = ''
		params = []
		frames = []
		# ------------------ handle uri, detach uri ------------------ #
		#
		# all format for uri:
		# 1: http://exame.com/folder1/folder2/?param1=xx
		# 2: http://exame.com:8080/folder1/folder2/?param1=xx
		# 3: https://exame.com/folder1/folder2/?param1=xx
		# 4: http://10.10.10.10/folder1/folder2/?param1=xx
		# 5: http://10.10.10.10:8080/folder1/folder2/?param1=xx
		# 6: https://10.10.10.10/folder1/folder2/?param1=xx
		# 7: exame.com:8080/folder1/folder2/?param1=xx
		# 8: 10.10.10.10/folder1/folder2/?param1=xx
		# 9: 10.10.10.10:8080/folder1/folder2/?param1=xx
		#
		# ------------------------------------------------------------ #
		if re.match('https://', uri):
			host, port, folder, file_name, extension, params, frames = self._detach_for_https(uri)
		elif re.match('http://', uri):
			host, port, folder, file_name, extension, params, frames = self._detach_for_http(uri)
		else:
			host, port, folder, file_name, extension, params, frames = self._detach_for_not_http(uri)

		self.domain = host
		self.port = port
		self.folder = folder
		self.file_name = file_name
		self.extension = extension
		self.params = params
		self.frames = frames
		
		return host, port, folder, file_name, extension, params, frames


	def _detach_for_https(self, uri):
		uri = uri.split("https://")[1]
		return self._detach_for_not_http(uri, port=443)


	def _detach_for_http(self, uri):
		uri = uri.split("http://")[1]
		return self._detach_for_not_http(uri)


	def _detach_for_not_http(self, uri, port=80):
		"""
			# 7: exame.com:8080/folder1/folder2/?param1=xx
			# 8: 10.10.10.10/folder1/folder2/?param1=xx
			# 9: 10.10.10.10:8080/folder1/folder2/?param1=xx#div1
		"""
		list_path_url = uri.split("/") # url: exame.com/aaaa/bbbb => ['exame.com', 'aaaa', 'bbbb']
		domain = ''
		# port  = 80
		folder = ''
		file_name = ''
		extension = ''
		params = []
		frames = []
		domain_port = list_path_url[0]
		domain = domain_port.split(":")[0]
		# port
		# print "uri: ",uri
		if len(domain_port.split(":")) > 1:
			try:
				port = int(domain_port.split(":")[1])
			except:
				port = 80

		return self._detach_element(list_path_url, domain=domain, port=port)

	def _detach_element(self, list_path_url, domain=None,port=None):
		# folder
		if len(list_path_url) >= 3:
			folder = ''.join ( '/' + _  for _ in list_path_url[1:-1])
		else:
			folder = '/'
		# file_name
		if len(list_path_url) > 1:
			file_name = list_path_url[-1:][0]
			if ("?" in file_name) or ("#" in file_name):
				file_name = file_name.split("?")[0]
				file_name = file_name.split("#")[0]
		else:
			file_name = ""

		#extension
		if file_name == '':
			extension = ''
		else:
			try:
				extension = file_name.split(".")[1]
			except:
				extension = ''
		#params
		if "?" in list_path_url[-1:][0]:
			params = re.findall('(\w+)=', list_path_url[-1:][0].split('#')[0])
		else:
			params = []

		# frame
		if "#" in list_path_url[-1:][0]:
			frames = re.findall('(\w+)=', list_path_url[-1:][0].split('#')[1])
		else:
			frames = []

		return domain, port, folder, file_name, extension, params, frames


	def get_url(self):
		"""
			return: full path uri
		"""
		if not re.match("http", self.url):
			if self.port==443:
				self.url = "https://{0}".format(self.url)
			else:
				self.url="http://{0}".format(self.url)
		if "?" in self.url:
			return self.url.split("?")[0]
		if "#" in self.url:
			return self.url.split("#")[0]
		return self.url


	def get_params(self, uri, param={}):
		"""
		:Return string all params
		"""
		_params = ""
		for var in self.params:
			_params += ", " + var
		return _params[2:]	


	def get_extension(self, uri):
		"""
			return: extension of uri
			priority: uri > self.url
		"""
		return self.extension


	def get_domain(self, uri=None):
		"""
			return: origin url.
			priority: uri > self.url
		"""
		if uri == None:
			return self.domain
		domain = ""
		return domain


	def set_params(self, param=None, list_params=None):
		"""
			set param. Only name
		"""
		self.params.append(param)
		if list_param!=None:
			self.params = list_params


	def set_domain(self, domain):
		self.domain = domain


	def set_extension(self, ext):
		self.extension = ext

	
	def set_url(self, url):
		self.url = url
	

	def set_port(self, port=80):
		"""
			set port: default 80
		"""
		self.port = port

	