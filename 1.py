import urllib.request
import lxml.html
import re

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = 'http://nr2.lt/blogs/Igor_Jakovenko/Petr-Tolstoy-sovershil-nacistskiy-kaming-aut-124626.html'
headers={'User-Agent':user_agent,} 

request = urllib.request.Request(url,None,headers) 
response = urllib.request.urlopen(request)

html = response.read().decode('utf-8')
response.close()

tree = lxml.html.fromstring(html)

title = tree.xpath('.//title/text()')
for line in title:
    line = line.strip('/ NEWSROOM')

author = tree.xpath('.//div[@class="author"]/text()')

date = tree.xpath('.//time')[0].get('datetime')

paragraph = tree.xpath('.//div/p/text()')
for text in paragraph:
    text = text.replace('\xa0', '')
    words = text.split()
    print (len(words))

