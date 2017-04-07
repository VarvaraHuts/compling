##скачивание постов со стены одной популярной телепередачи

import urllib.request
import json
import sys

s = open('posts.txt', 'w', encoding = 'utf-8')
f = open('comments.txt', 'w', encoding = 'utf-8')

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
id_arr = []

for i in range(201):
    try:
        url = 'https://api.vk.com/method/wall.get?owner_id=-37008294&count=1' + '&offset=' + str(i)
        res = urllib.request.urlopen(url).read().decode('utf-8').translate(non_bmp_map)
        data = json.loads(res)
        text = data['response'][1]['text']
        s.write(text + '\n')

        post_id = data['response'][1]['id']
        id_arr.append(post_id)
    except: 
        pass
s.close()

for x in id_arr:
    for y in range(101):
        try:
            url_com = 'https://api.vk.com/method/wall.getComments?owner_id=-37008294&post_id=' + str(x) + '&count=1' + '&offset=' + str(y)
            res_com = urllib.request.urlopen(url_com).read().decode('utf-8').translate(non_bmp_map)
            data_com = json.loads(res_com)
            for k in range(1,10):
                text_com = data_com['response'][k]['text']
                f.write(text_com + '\n')
        except:
            pass
f.close()

a = open('posts.csv', 'w', encoding = 'Windows-1251')
z = open('comments.csv', 'w', encoding = 'Windows-1251')

b = open('posts.txt', 'r', encoding = 'utf-8')
lines = b.readlines()
for line in lines:
    line = line.replace('<br>', '')
    words = line.split()
    a.write(str(len(words)) + '\n')
a.close()

v = open('comments.txt', 'r', encoding = 'utf-8')
lines = v.readlines()
for line in lines:
    words = line.split()
    z.write(str(len(words)) + '\n')
z.close()
        

