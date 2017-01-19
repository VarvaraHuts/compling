s = input()

def create_array(s):
    words = []
    while s:
        if len(s) == 0:
            break
        words.append(s)
        s = input()
    return(words)

def reverse_words(words):
    words.reverse()
    return (words)

def main():
    val = create_array(s)
    print(reverse_words(val))

if __name__ == '__main__':
    main()
