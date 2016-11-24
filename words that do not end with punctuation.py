f = open('C:/Python34/readfile.txt')
lines = f.readlines()
words = []
for line in lines:
    words.append(line.strip().split(' '))
a = 0
for line in words:
    for word in line:
        if word[len(word)-1] != '.' and word[len(word)-1] != ',':
            a += 1
print (a)

        
