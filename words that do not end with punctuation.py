f = open('1.txt')
lines = f.read()
words = lines.split()
punct = ',.'
count = 0
for word in words:
    for i in punct:
        if word.endswith(i):
            count += 1
print ((len(words) - count)*100/len(words))

