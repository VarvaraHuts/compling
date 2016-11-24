arr = []
s = input()
while len(s) > 0:
    arr.append(s)
    s = input()
arr.reverse()
for s in arr:
    print (s)
