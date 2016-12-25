def createDic():
    dic = {'ა':'ɑ','ბ':'b','გ':'g','დ':'d','ე':'ɛ','ვ':'v','ზ':'z',
       'ი':'ɪ','ლ':'l','მ':'m','ნ':'n','ო':'ɔ','ჟ':'ʒ','რ':'r',
       'ს':'s','ჳ':'w','უ':'u','ღ':'ʁ','შ':'ʃ','ხ':'χ','ჴ':'q',
       'ჰ':'h','თ':'tʰ','კ':'kʼ','პ':'pʼ','ტ':'tʼ','ფ':'pʰ',
       'ქ':'kʰ','ყ':'qʼ','ჩ':'t͡ʃ','ც':'t͡s','ძ':'d͡z','წ':'t͡sʼ',
       'ჭ':'t͡ʃʼ','ჯ':'d͡ʒ'}
    return (dic)

def transliterate():
    f = open('грузинский. текст.txt', 'r', encoding = 'utf-8')
    f1 = f.read()
    f.close()
    for key, value in createDic().items():
        f1 = f1.replace(key, value)
    return(f1)

if __name__ == '__main__':
    print (transliterate())
