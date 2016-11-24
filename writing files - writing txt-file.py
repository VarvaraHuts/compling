f = open('1.txt', 'w', encoding = 'utf-8')
s = input ()
while True:
    if s == 'stop':
        break
    f.write(s)
    s = input ()
f.close()
