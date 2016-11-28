import re
f = open ('1.txt', 'r', encoding = 'utf-8')
s = ' '.join(f)
words = s.split()
r = '(б[аоуеиюяёы])'
for word in words:
    if re.search (r, word):
        res = re.search(r, word)
        print (res.group(1))
