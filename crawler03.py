#!/usr/bin/python

import urllib2
import re

def GetBlog():
	mainUrl = 'http://www.zreading.cn/archives/'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent}
	for i in range(6,20):
		url = mainUrl+ str(i) +'.html'
		print 'visiting...' + url
		req = urllib2.Request(url, headers = headers) 
		try:
			res = urllib2.urlopen(req)
			blogPage = res.read()
			mainItem = re.findall('<article.*?class="entry-common".*?</article>', blogPage,re.S)
			if len(mainItem) > 0:
				Dowith(mainItem[0])
		except Exception as e:
			print type(e)


def Dowith(raw_content):
	title = re.findall('<h2 class="entry-name".*?</h2>',raw_content,re.S)
	if len(title) > 0:
		title[0] = re.sub('<.*?>','',title[0])
	else:
		print "Can't find anything"
		exit()
	raw_content = re.sub('<div id="crumb".*?div>','',raw_content)
	raw_content = raw_content.replace("\n","").replace("<p>","    ").replace("</p>","\n\n").replace("<strong>","").replace("</strong>","")
	content = re.sub('<.*?>','',raw_content)
	Tostore(content,title[0].replace(' ',''))

def Tostore(content,title):
	f = file(title, 'w')
	f.write(content)
	f.close

if __name__== "__main__":	
	GetBlog()
