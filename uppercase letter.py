f = open('1.txt')
f = f.read()
words = f.split()
count_words = 0
for word in words:
    letter = word[0]
    if letter.isupper():
        count_words += 1
print (count_words)
