s = input()
lst = []
while s:
    if len(s) == 0:
        break
    lst.append(s)
    s = input()
lst.reverse()
for word in lst:
    print (word, end='\n')
