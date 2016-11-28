import re
f = open ('1.txt', encoding = 'utf-8')
s = f.read()
s1 = re.sub('([а-я]+?) ([а-я]+?)', r'\2 \1', s)
print (s1)
