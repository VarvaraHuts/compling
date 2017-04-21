import urllib.request
import sys
import json
import sqlite3
import datetime

con = sqlite3.connect('VK_test.db')
cur = con.cursor()

cur.execute('CREATE TABLE publics (id_public INTEGER PRIMARY KEY, ids_posts VARCHAR(30))')
cur.execute('CREATE TABLE posts (id_post INTEGER PRIMARY KEY, id_public INTEGER, ids_comments VARCHAR(30))')
cur.execute('CREATE TABLE comments (id_comment INTEGER PRIMARY KEY, id_reply VARCHAR(30), text VARCHAR(300), time VARCHAR(30), id_user INTEGER)')
cur.execute('CREATE TABLE users (id_user INTEGER PRIMARY KEY, city INTEGER, bdate VARCHAR(30))')
con.commit()

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def get_comments_ids(post_id):
    com_ids = []
    for x in range(100):
        try:
            url_com = 'https://api.vk.com/method/wall.getComments?owner_id=-' + str(id_public) + '&post_id=' + post_id + '&count=1&offset=' + str(x)
            res_com = urllib.request.urlopen(url_com).read().decode('utf-8').translate(non_bmp_map)
            data_com = json.loads(res_com)
            cid = str(data_com['response'][1]['cid'])
            com_ids.append(cid)
            text_com = data_com['response'][1]['text']
            if '<br>' in text_com:
                text_com = text_com.replace('<br>', '')
            if text_com == '':
                text_com = 'n/a'
            date_com = data_com['response'][1]['date']
            time_com = datetime.datetime.fromtimestamp(date_com).strftime('%Y-%m-%d %H:%M:%S')
            id_user = data_com['response'][1]['from_id']
            try:
                id_reply_to = str(data_com['response'][1]['reply_to_uid'])
            except:
                id_reply_to = 'n/a'
            cur.execute('INSERT OR IGNORE INTO comments VALUES (?, ?, ?, ?, ?)', (int(cid), id_reply_to, text_com, time_com, id_user))

            url_user = 'https://api.vk.com/method/users.get?user_ids=' + str(id_user) + '&fields=bdate,city'
            res_user = urllib.request.urlopen(url_user).read().decode('utf-8').translate(non_bmp_map)
            data_user = json.loads(res_user)
            city = data_user['response'][0]['city']
            bdate = str(data_user['response'][0]['bdate'])
            if bdate == '':
                bdate = 'n/a'
            cur.execute('INSERT OR IGNORE INTO users VALUES (?, ?, ?)', (id_user, city, bdate))
            con.commit()
        except:
            pass
    com_ids_str = ", ".join(com_ids)
    return com_ids_str

def get_posts_ids(id_public):
    post_ids = []
    for i in range(700):
        url = 'https://api.vk.com/method/wall.get?owner_id=-' + str(id_public) + '&count=1&offset=' + str(i)
        res = urllib.request.urlopen(url).read().decode('utf-8').translate(non_bmp_map)
        data = json.loads(res)
        post_id = str(data['response'][1]['id'])
        post_ids.append(post_id)
        ids_comments = get_comments_ids(post_id)
        cur.execute('INSERT OR IGNORE INTO posts VALUES (?, ?, ?)', (int(post_id), int(id_public), ids_comments))
        con.commit()
    post_ids_str = ", ".join(post_ids)
    return post_ids_str


ids_publics = ['37008294', '138990001']
for id_public in ids_publics:
    ids_posts = get_posts_ids(id_public)
    cur.execute('INSERT OR IGNORE INTO publics VALUES (?, ?)', (int(id_public), ids_posts))
    con.commit()
    
con.close()
