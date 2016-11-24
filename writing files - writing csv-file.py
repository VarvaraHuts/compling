f = open('1.csv', 'w', encoding = 'utf-8')
s = input ()
while True:
    if s == 'stop':
        break
    x = len(s) - 1
    i = 0
    while x - 1 >= i:
        if s[x - i] == s[i]:
            a = 'yes'
            i += 1
        else:
            a = 'no'
            break
    if s.endswith ('ed'):
        b = 'yes'
    else:
        b = 'no'
    f.write(s + ',' + str(len(s)) + ',' + a + '\n')
    s = input ()
f.close()



