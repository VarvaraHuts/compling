import random
index = [0, 1, 2, 3]

def split_words():
    f = open ('дз1. словарь.txt', encoding = 'utf-8')
    f = f.read()
    words = f.split()
    return(words)

def slotSubj(words):
    subj = []
    for word in words:
        if word.endswith('а') or word.endswith('я'):
            subj.append(word)
    i = random.choice(index)
    return (subj[i])

def slotVerb(words):
    verb = []
    for word in words:
        if word.endswith('ит') or word.endswith('ет') or word.endswith('ёт'):
            verb.append(word)
    j = random.choice(index)
    return (verb[j])

def slotObj(words):
    obj = []
    for word in words:
        if word.endswith('у') or word.endswith('и'):
            obj.append(word)
    k = random.choice(index)
    return(obj[k])

def main():
    val = split_words()
    print (slotSubj(val)+ ' ' + slotVerb(val) + ' ' + slotObj(val))

if __name__ == '__main__':
    main()
    
    






