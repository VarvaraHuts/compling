import urllib.request
import lxml.html
import re
import os
from datetime import timedelta, date


table = open("table.csv", "w", encoding = "Windows-1251")


user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
headers = {"User-Agent":user_agent,} 

start_date = date(2017, 2, 26)
end_date = date(2017, 2, 27)

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield (start_date + timedelta(n))

        
for single_date in daterange(start_date, end_date):
    
    date = single_date.strftime("%Y/%m/%d")
    link = "https://lenta.ru/" + date
    request = urllib.request.Request(link,None,headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    response.close()

    links_articles = re.findall("articles/" + date + ".+?/", html)
    links_news = re.findall("news/" + date + ".+?/", html)
    links = []
    for link_article in links_articles:
        if link_article not in links:
            links.append(link_article)
    for link_news in links_news:
        if link_news not in links:
            links.append(link_news)


    for link in links:
        
        url = "https://lenta.ru/" + link
        try:
            f = urllib.request.urlopen(url)
        except urllib.request.HTTPError as e:
            if e.code == 404:
                continue
        html_page = f.read().decode('utf-8')
        tree = lxml.html.fromstring(html_page)

        title = tree.xpath('.//title/text()')
        for line in title:
            line = re.findall(".+?:", line)
        title = line[0].strip(":") ### транслитерация
        if "?" in title:
            title = title.strip("?")

        author = tree.xpath('.//span[@class="name"]/text()')### author
        for line in author:
            line = line.strip("Беседовал ")
        author = line

        article = tree.xpath('.//div/p/text()')
        article = "J".join(article)
        article = article.replace("J", "\n")

        tokens = article.split( )
        words = []
        for token in tokens:
            if token != "—":
                words.append(token)
        wordcount = len(words)

        ### source

        path = 'C:/Users/Desktop/lenta' + date[0:7]
        if not os.path.exists(path):
            os.makedirs(path)
        file = open(path + "/" + title + ".txt", "w", encoding = "utf-8")
        file.write(article)
        file.close()


table.close()


        

        

       


        





    
    

