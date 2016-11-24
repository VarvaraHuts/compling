f = open('C:/Python34/readfile.txt')
lines = f.readlines()
words = []
for line in lines:
    words.append(line.strip().split(' '))
a = 0
for line in words:
    for word in line:
        if len(word) == 3:
            a += 1
b = 0
for line in words:
    for word in line:
        if len(word) == 1:
            b += 1
print (a/b)
