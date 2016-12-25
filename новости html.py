import re
import os
for fname in os.listdir('html'):
    file = open ('html/' + fname, 'r', encoding = 'utf-8')
    s = file.read()
    text = re.sub('<.*?>', ' ', s)
    print (text)
    

    



