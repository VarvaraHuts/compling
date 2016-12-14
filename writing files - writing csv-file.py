f = open('1.csv', 'w', encoding = 'utf-8')
s = input ()
while True:
    if s == 'stop':
        break
    for i in range (len (s) - 1):
        if s[i] == s[len(s) - 1 - i]:
            a = '+ palyndrome'
        else:
            a = '- palyndrome'
    if s.endswith ('ed'):
        b = '+ verb'
    else:
        b = '- verb'
    f.write(s + ',   ' + str(len(s)) + ',   ' + a + ',   ' + b + '\n')
    s = input ()
f.close()




