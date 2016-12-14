f = open('C:/Python34/readfile.txt')
lines = f.readlines()
for i in range (len(lines)):
    if i % 2 == 1:
        print (lines[i])

    
