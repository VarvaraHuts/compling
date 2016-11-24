a = 1
while a <= 3:
    print('Hello!' * a)
    a += 1

i = 0
while i < 10:
    print (i)
    i += 1

i = 0
while i < 10:
    i += 1
    print (i)

i = 0
while i <= 10:
    i += 1
    if i > 7:
        i += 2
    print (i)

a = 5
while a <= 55:
    print (a)
    a += 2

a = 5
while a <= 55:
    if a % 2 == 1:
        print (a)
    a += 1

n = int (input ())
c = 1
while c <= n:
    print ('*' * c)
    c += 1

n = int (input ())
stars = '*'
while len (stars) <= n:
    print (stars)
    stars += '*'

i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i += 1

a = int (input ())
b = int (input ())
i = a
while i <= b:
    sum += i
    i += 1
print (sum)

sum = 0
s = int (input ())
while s != 0:
    sum += s
    s = int (input ())
if s == 0:
    print (sum)


a = int(input())
b = int(input())
d = 1
while d % a != 0 or d % b != 0:
    d+=1
print(d)
