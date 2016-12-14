f = open('C:/Python34/readfile.txt')
lines = f.readlines()
lst = []
for line in lines:
  length = len(line)
  lst.append(length)
print (max(lst) / min (lst))
