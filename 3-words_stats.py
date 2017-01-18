from collections import Counter

text = open('otters.txt', 'r', encoding='utf-8')
text = text.read()

def count_words(text):
    text = text.lower()
    skips = ['.', ',', ':', ';', '—', '"', '?', '!']
    for ch in skips:
        text = text.replace(ch, '')
    word_counts = Counter(text.split(' '))
    return (word_counts)

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

word_stats(word_counts)
