import urllib.request

resp = urllib.request.urlopen('http://www.lib.ru/LITRA/CHEHOW/kashtanka.txt')
html = resp.read().decode('utf-8')
resp.close()

