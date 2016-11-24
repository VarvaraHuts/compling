n = input ()
cnt1 = 0
for i in n:
    if i == 'g':
        cnt1 += 1
cnt2 = 0
for j in n:
    if j == 'c':
        cnt2 += 1
print ((cnt1 + cnt2) / len (n) * 100)
