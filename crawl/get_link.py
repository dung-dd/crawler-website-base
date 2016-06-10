import re
"""
	Only get Open tag need
	example:
		<button attr="value"> -> not <button attr="value"> text </button>
"""
class get_link():
	def __init__(self, response, domain, port, folder):
		self.domain = domain
		self.port = port
		self.folder = folder
		self.links = [] # we need
		self.tag_a = []
		self.tag_link = []
		self.tag_form = []
		self.tag_script = []
		self.all_tag = self.get_all_tag(response)
		self.get_link_tag_a()
		self.get_link_tag_link()
		self.get_link_tag_script()
		self.get_link_in_tag_form()
		

	def get_all_tag(self, response):
		"""
			Get all TAG in response, only open tag, not have content
			includes tag_name, attributes
		"""
		all_tag = [] # only open tag, not have content in tag 
		all_tag = re.findall('(<[^<]+>)', response)

		for tag in all_tag:
			if re.match("<a", tag):
				self.tag_a.append(tag)
			elif re.match("<link", tag):
				self.tag_link.append(tag)
			elif re.match("<form", tag):
				self.tag_form.append(tag)
			elif re.match("<script", tag):
				self.tag_script.append(tag)


	def get_link_tag_a(self):
		"""	
			:response: response use get link
			:domain: check same domain
			:folder: folder of resource have response
			get all link in tag <a></a>
			:return all link in tag <a></a>
		"""
		tag_a = self.tag_a
		links = []
		for tag in tag_a:
			if re.search("href=(\"|')(\S+)(\"|')", tag):
				link = re.search("href=(\"|')(\S+)(\"|')", tag).group(2)
				links.append(self.real_link(link))
		self.links .extend(links)


	def get_link_tag_script(self):
		"""	
		"""
		tag_script = self.tag_script
		links = []
		for tag in tag_script:
			if re.search("src=(\"|')(\S+)(\"|')", tag):
				link = re.search("src=(\"|')(\S+)(\"|')", tag).group(2)
				links.append(self.real_link(link))
		self.links .extend(links)


	def get_link_tag_link(self):
		"""
		"""
		tag_link = self.tag_link
		links = []
		for tag in tag_link:
			if re.search("href=(\"|')(\S+)(\"|')", tag):
				link = re.search("href=(\"|')(\S+)(\"|')", tag).group(2)
				links.append(self.real_link(link))
		self.links .extend(links)


	def get_link_in_tag_form(self):
		"""	
		"""
		tag_link = self.tag_link
		links = []
		for tag in tag_link:
			if re.search("action=(\"|')(\S+)(\"|')", tag):
				link = re.search("href=(\"|')(\S+)(\"|')", tag).group(2)
				links.append(self.real_link(link))
		self.links .extend(links)
		

	def real_link(self, link):
		if re.match('http', link):
			# http://domain.com/folder/file.php
			# http://difficultdomain.com/folder/file.php
			if self.domain in link:
				return link
			else:
				return None
		else:
			# /folder/file.php
			# ../../folder/file.php
			if ".." in link:
				parents = re.findall('(\.\.)', link)
				f = folder.split("/")
				folder = ''+"".join("/" + _ for _ in f[:-len(parents)])
				link = re.sub("(\.\./){1,}","/", link)
			if self.port == 443:
					new_url = "https://{0}{1}{2}".format(self.domain, self.folder, link)
			elif self.port==80:
				new_url = "http:///{0}{1}{2}".format(self.domain, self.folder, link)
			else:
				new_url = "http://{0}:{1}{2}{3}".format(self.domain, self.port, self.folder, link)
			return new_url.replace("//","/")


	def get_link_tag_button(self):
		"""	
		"""
		links = []
		self.links .extend(links)


	def getResults(self):
		return self.links