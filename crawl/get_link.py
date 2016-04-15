import re
"""
	Only get Open tag need
	example:
		<button attr="value"> -> not <button attr="value"> text </button>
"""


def real_link(link, domain, port, folder):
	if re.match('http', link):
		# http://domain.com/folder/file.php
		# http://difficultdomain.com/folder/file.php
		if domain in link:
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
		if port == 443:
				new_url = "https://{0}{1}{2}".format(domain, folder, link)
		elif port==80:
			new_url = "http:///{0}{1}{2}".format(domain, folder, link)
		else:
			new_url = "http://{0}:{1}{2}{3}".format(domain, port, folder, link)
		return new_url.replace("//","/")


def get_link_tag_a(response, domain, port, folder):
	"""	
		:response: response use get link
		:domain: check same domain
		:folder: folder of resource have response
		get all link in tag <a></a>
		:return all link in tag <a></a>
	"""
	f = open("test.txt","a")
	f.write("----------------- "+folder+" ---------------------")
	f.write(response)
	f.close()
	tags = re.findall('<a \S+>', response)
	f = open("test.txt","a")
	f.write(response)
	f.close()
	links = []
	for tag in tags:
		if re.search("href=(\"|')(\S+)(\"|')", tag):
			link = re.search("href=(\"|')(\S+)(\"|')", tag).group(2)
			links.append(real_link(link, domain, port, folder))

	# check folder and add to links
	# will return http://domain.com/link
	# format all link in links: http://domain.com/link
	return links


def get_link_tag_link(response, domain, port, folder):
	"""	
		:response: response use get link
		:domain: check same domain
		:folder: folder of resource have response
		get all link in tag <link></link>
		:return all link in tag <link></link>
	"""
	pass


def get_link_tag_button(response, domain, port, folder):
	"""	
		:response: response use get link
		:domain: check same domain
		:folder: folder of resource have response
		get all link in tag <button></button>
		:return all link in tag <button></button>
	"""
	tags = re.findall('(<button \S+>)', response)
	pass


def get_link_in_tag_form(response, domain, port, folder):
	"""	
		:response: response use get link
		:domain: check same domain
		:folder: folder of resource have response
		get all link in tag <button></button>
		:return all link in tag <button></button>
	"""
	pass
	
