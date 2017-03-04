import urllib.request
import lxml.html
import re
import os
from datetime import timedelta, date
from pymystem3 import Mystem

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield (start_date + timedelta(n))

def getLinks(source_path, headers, date):

    link = source_path + date
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
    return links


def getArticleInfo(html_tree):
    title = html_tree.xpath('.//title/text()')
    for line in title:
        line = re.findall(".+?:", line)
    title = line[0].strip(":") 
    if '?' in title:
            title = title.replace('?', '')
    if ':' in title:
        title = title.replace(':', '')
    if '*' in title:
        title = title.replace('*', '')
    if '"' in title:
        title = title.replace('"', '')
    if "'" in title:
        title = title.replace("'", '')
    if '#' in title:
        title = title.replace('#', '')
    if '«' in title:
        title = title.replace('«', '')
    if '»' in title:
        title = title.replace('»', '')
        
    author = html_tree.xpath('.//span[@class="name"]/text()')
    if len(author) > 0:
        for line in author:
            line = line.replace("Беседовал ", "")
            line = line.replace("Беседовала ", "")
            line = line.replace("Беседовали ", "")
            line = line.replace("Записал ", "")
            line = line.replace("Записала ", "")
            line = line.replace("Записали ", "")
            line = line.replace("Подготовил ", "")
            line = line.replace("Подготовила ", "")
            line = line.replace("Подготовили ", "")
        author = line
    else:
        author = "не указан"

    article = html_tree.xpath('.//div/p/text()')
    article = "\n".join(article)
    return author, title, article


def processNews(source_path, source_name, headers, start_date, end_date, filesFolderPathPrefix, table_path):
    for single_date in daterange(start_date, end_date):
        date = single_date.strftime("%Y/%m/%d")
        links = getLinks(source_path, headers, date)

        for link in links:
            url = source_path + link
            try:
                f = urllib.request.urlopen(url)
            except urllib.request.HTTPError as e:
                if e.code == 404:
                    continue
            html_page = f.read().decode('utf-8')
            tree = lxml.html.fromstring(html_page)

            author, title, article = getArticleInfo(tree)

            tokens = article.split()
            words = []
            for token in tokens:
                if token != "—":
                    words.append(token)
            wordcount = len(words)

            path = filesFolderPathPrefix + date[0:7]
            if not os.path.exists(path):
                os.makedirs(path)
            file = open(path + "/" + title + ".txt", "w", encoding = "utf-8")
            file.write(article)
            file.close()

            m = Mystem()
            lemmas = m.lemmatize(article)
            article_lemmatized = ''.join(lemmas)
            article_analyzed = m.analyze(article)

            path2 = filesFolderPathPrefix + date[0:7] + ' ' + 'mystem'
            if not os.path.exists(path2):
                os.makedirs(path2)
            file_mystem = open(path2 + "/" + title + ".txt", 'w', encoding = "utf-8")
            file_mystem.write(article_lemmatized + '\n' + '\n' + '\n' + str(article_analyzed))
            file_mystem.close()

            table.write(";".join([source_name, path, author, date, title, url, str(wordcount)]) + "\n")
            table.close()


if __name__ == "__main__":
    source_path = "https://lenta.ru/"
    source_name = "Lenta.ru"
    user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
    headers = {"User-Agent": user_agent, }
    start_date = date(2015, 7, 1)
    end_date = date(2016, 12, 31)
    filesFolderPathPrefix = 'C:/Users/Desktop/lenta'
    table = open('table.csv', "w", encoding = "Windows-1251")
    processNews(source_path, source_name, headers, start_date, end_date, filesFolderPathPrefix, table)


        

        

       


        





    
    

