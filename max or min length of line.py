f = open('C:/Python34/readfile.txt')
lines = f.readlines()
print (max (len (line) for line in lines) / min (len (line) for line 
in lines))
