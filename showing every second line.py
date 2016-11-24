f = open('C:/Python34/readfile.txt')
lines = f.readlines()
for i in range (len(lines)):
    if i % 2 == 0:
        print (lines[i])

    
