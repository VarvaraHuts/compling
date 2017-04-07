##скачивание постов со стены одной популярной телепередачи

import urllib.request
import json
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def write_vk_info_to_text_file(filename, url, count, is_post):
    ids = []
    s = open(filename, 'a', encoding='utf-8')
    for i in range(count):
        url_extended = url + str(i)
        try:
            res = urllib.request.urlopen(url_extended).read().decode('utf-8').translate(non_bmp_map)
            data = json.loads(res)
            if is_post:
                text = data['response'][1]['text']
                s.write(text + '\n')
                post_id = data['response'][1]['id']
                ids.append(post_id)
            else:
                for k in range(1, 10):
                    text_com = data['response'][k]['text']
                    s.write(text_com + '\n')
        except:
            pass

    s.close()
    return ids


def write_from_txt_to_csv(filename_txt, filename_csv, is_post):
    a = open(filename_csv, 'w', encoding='Windows-1251')
    b = open(filename_txt, 'r', encoding='utf-8')
    lines = b.readlines()
    for line in lines:
        if is_post:
            line = line.replace('<br>', '')
        words = line.split()
        a.write(str(len(words)) + '\n')
    a.close()
    b.close()


if __name__ == "__main__":
    ids = write_vk_info_to_text_file('posts.txt',
                                'https://api.vk.com/method/wall.get?owner_id=-37008294&count=1&offset=',
                                201,
                                True)
    for x in ids:
        write_vk_info_to_text_file('comments.txt',
                              'https://api.vk.com/method/wall.getComments?owner_id=-37008294&post_id=' +
                              str(x) + '&count=1&offset=',
                              101,
                              False)

    write_from_txt_to_csv('posts.txt', 'posts.csv', True)
    write_from_txt_to_csv('comments.txt', 'comments.csv', False)

