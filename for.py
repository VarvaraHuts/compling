a = 3115
b = 9441
sum = 0
for i in range (a, b + 1):
    if i%2 == 1:
        sum += i
print (sum)

a = 3115
b = 9441
sum = 0
if a % 2 == 0:
    a += 1
for i in range (a, b + 1, 2):
    s += i
print (s)

a, b = (int(i) for i in input().split())
sum = 0
if a % 2 == 0:
    a += 1
for i in range (a, b + 1, 2):
    s += i
print (s)

for i in range (3):
    for j in range (3):
        print ('*', end = '')

a = 'ABCD'
for i in range (4):
    print (a[i])

a = 'ABCD'
for b in a:
    print (b)

genome = input()
cnt = 0
for nucl in genome:
    if nucl == 'C':
        cnt += 1
print (cnt)

a = int (input ())
b = int (input ())
s = j = 0
for i in range (a, b + 1):
    if i % 3 == 0:
        s += i
        j += 1
print (s/j)

