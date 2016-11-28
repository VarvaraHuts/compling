import re
f = open ('1.txt', encoding = 'utf-8')
s = f.read()
s1 = re.sub('[а-я]', 'о', s)
print (s1)
