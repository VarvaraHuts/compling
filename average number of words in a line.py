f = open('C:/Python34/readfile.txt')
lines = f.readlines()
words = []
for line in lines:
    words.append(line.strip().split(' '))
average = sum(len(line) for line in words) / len(words)
print (average)

        
