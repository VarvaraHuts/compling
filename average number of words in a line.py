f = open('C:/Python34/readfile.txt')
lines = f.readlines()
countlines = len(lines)
countwords = 0
for line in lines:
    words = line.strip()
    numwords = len(words)
    countwords += numwords
print (countwords/countlines)
        
