import urllib.request
import re

f = urllib.request.urlopen('https://russian.rt.com/')
html = f.read().decode('utf-8')
f.close()

links = re.findall ('<a class="link " href="/world/article/.+?>', html)

for link in links:
    link = link.strip('<a class="link " href="')
    link = link.strip('">')
    link = 'https://russian.rt.com' + link
    f1 = urllib.request.urlopen(link)
    html1 = f1.read().decode('utf-8')
    f1.close()
    html1 = html.lower()
    html1 = html1.split()
    words = []
    for item in html1:
        if re.search ('[а-яА-Я]', item):
            words.append(item)
    dic = {}
    for word in words:
        word = word.strip(',.:;"?!.«»&<>/-=_()abcdefghijklmnopqrstuvwxyz')
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    for key, value in sorted(dic.items()):
        print (key + ' ' + str(value))


        
    




