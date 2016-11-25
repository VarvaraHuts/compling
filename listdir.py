s = open('1.csv', 'w', encoding = 'utf-8')
import os
d = {}
countFiles = {}
for fname in os.listdir ('folder'):
    f = open ('folder/' + fname, 'r', encoding = 'utf-8')
    f = ' '.join(f)
    words = f.split()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    words = set (words)
    for word in words:
        if word in countFiles:
            countFiles[word] += 1
        else:
            countFiles[word] = 1
for key, value in d.items():
    s.write (key + ',' + str(value) + ',' + str(countFiles[key]))
s.close()  
            
            
            
        
        


