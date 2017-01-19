s = input ()

def lang(s):
    vowels = 'aeiouy'
    lastLetter = s[len(s)-1]
    for Letter in s:
        if Letter in vowels and Letter != lastLetter:
            print ('no')
        else:
            print ('yes')
    return

lang(s)

