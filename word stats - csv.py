import os

def create_dic():
    dic = {}
    for fname in os.listdir ('folder'):
        f = open ('folder/' + fname, 'r', encoding = 'utf-8')
        f = f.read()
        words = f.split()
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
    return (dic)

def count_files():
    count_files = {}
    for fname in os.listdir ('folder'):
        f = open ('folder/' + fname, 'r', encoding = 'utf-8')
        f = f.read()
        words = f.split()
        words = set (words)
        for word in words:
            if word not in count_files:
                count_files[word] = 1
            else:
                count_files[word] += 1
    return (count_files)

def write_csv(dic, count_files):
    s = open('1.csv', 'w', encoding = 'utf-8')
    for key, value in dic.items():
        s.write (key + ',' + str(value) + ',' + str(count_files[key]))
    s.close()
    return (s)

def main():
    val1 = create_dic()
    val2 = count_files()
    write_csv(val1, val2)

if __name__ == '__main__':
    main()
           
            
            
            
            
            
        
        


