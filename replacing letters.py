s = list (input ())

def replace_Letter(s):
    for i in range (len(s)):
        if i % 2 == 1:
            s[i] = 'b'
    s = ''.join(s)
    print (s)
    return
replace_Letter(s)
