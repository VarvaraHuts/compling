import re
f = open ('1.txt', 'r', encoding = 'utf-8')
s = ' '.join(f)
words = s.split()
count = len(words)
i = 0
for word in words:
    if re.search ('[а-яё]', word):
        i += 1
if count != i:
    print (i, count)
else:
    print (count)
print (re.search('[а-яё]', word))
