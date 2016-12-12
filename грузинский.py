def openFile():
    f = open('1.txt', 'r', encoding = 'utf-8')
    f1 = f.read()
    f.close()
    f1 = list(f1)
    return (f1)

def transliterate():
    s = open('2.txt', 'r', encoding = 'utf-8')
    s1 = s.read()
    s.close()
    letters = s1.split()
    dic = {}
    for indx in range (len(letters)):
        if indx % 2 == 0:
            key = letters[indx]
        else:
            value = letters[indx]
        value = dic[key]
    return(dic)

print (transliterate())
        

