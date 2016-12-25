import random
index = [0, 1, 2, 3]

def openFile():
    f = open ('дз1. словарь.txt', encoding = 'utf-8')
    f = f.read()
    words = f.split()
    return(words)

def slotSubj():
    subj = []
    for word in openFile():
        if word.endswith('а') or word.endswith('я'):
            subj.append(word)
    i = random.choice(index)
    return (subj[i])

def slotVerb():
    verb = []
    for word in openFile():
        if word.endswith('ит') or word.endswith('ет') or word.endswith('ёт'):
            verb.append(word)
    j = random.choice(index)
    return (verb[j])

def slotObj():
    obj = []
    for word in openFile():
        if word.endswith('у') or word.endswith('и'):
            obj.append(word)
    k = random.choice(index)
    return(obj[k])

def createSent():
    slot1 = slotSubj()
    slot2 = slotVerb()
    slot3 = slotObj()
    return(slot1 + ' ' + slot2 + ' ' + slot3)

if __name__ == "__main__":
    print (createSent())
    
    






