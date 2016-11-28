import re
r = '[аоуеиюяэёы]'
f = open ('1.txt', encoding = 'utf-8')
s = f.read()
a = re.findall (r, s)
print (len(a))
