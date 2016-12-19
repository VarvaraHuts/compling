import os
import re
for file in os.listdir('html'):
    f = open ('html/' + file, 'r', encoding = 'utf-8')
    f = f.read()
    words = f.split()
    tags = []
    text = []
    r = '(\<*[A-Za-z]\>*)'
    r2 = '([/<])'
    r3 = '([-->])'
    r4 = '[{}+?&]'
    for word in words:
        if re.search (r, word):
            tags.append(word)
        elif re.search (r2, word):
            tags.append(word)
        elif re.search (r3, word):
            tags.append(word)
        elif re.search(r4, word):
            tags.append(word)
        else:
            text.append(word)
    text = ' '.join(text)
    print (text)
    

    



