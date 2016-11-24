i = 0
while i < 5:
    a, b = input().split()
    a = int (a)
    b = int (b)
    if a == 0 and b == 0:
        break
    if a == 0 or b == 0:
        break
    print (a*b)
    i += 1

while True:
    s = int (input ())
    if s < 10:
        continue
    elif s > 100:
        break
    else:
        print (s)



