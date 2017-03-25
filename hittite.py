f1 = open("syllab.html", "r", encoding="utf-8")
string = f1.read()
f1.close()

automata = [(1, {"other":37, "U":2, "Ú":2, "T":2, "K":2, "R":2, "É":2, "I":2, "N":2, "<":3, " ":21, "\n":21}),
            (2, {"eps":1}),
            (3, {"i":4, "s":11, "h":25, "other":20}),
            (4, {">":5, "other":20}),
            (5, {" ":22, "\n":22, "other":5, "m":6, "a":6, "n":6, "k":6, "u":6, "w":6, "p":6, "í":6, "š":6,
                "i":6, "l":6, "ḫ":6, "z":6, "d":6, "e":6, "t":6, "r":6, "á":6, "Š":7, "I":7, "A":7, "<":8}),
            (6, {"eps":5}),
            (7, {"eps":5}),
            (8, {'/':9, 'other':20}),
            (9, {'i':10, 'other':20}),
            (10, {'>':1, 'other':20}),
            (11, {'u':12, 'other':20}),
            (12, {'p':13, 'other':20}),
            (13, {'>':14, 'other':20}),
            (14, {"other":36, " ": 15, 'd':15, "L":15, "Ú":15, "M":15, "E":15, "Š":15, "<":24, "/":16}),
            (15, {"eps":14}),
            (16, {'s':17, "other":24}),
            (17, {'u':18, "other":24}),
            (18, {'p':19, "other":24}),
            (19, {'>':1, "other":24}),
            (20, {">":1, "other":20}),
            (21, {"eps":1}),
            (22, {"eps":5}),
            (23, {"eps":14}),
            (24, {">":14, "other":24, "/":16}),
            (25, {'e':26, 'other':20}),
            (26, {'a':27, 'other':20}),
            (27, {'d':28, 'other':20}),
            (28, {'>':29, 'other':20}),
            (29, {'<':30, 'other':29}),
            (30, {'/':31, 'other':29}),
            (31, {'h':32, 'other':29}),
            (32, {'e':33, 'other':29}),
            (33, {'a':34, 'other':29}),
            (34, {'d':35, 'other':29}),
            (35, {'>':1, 'other':29}),
            (36, {"<": 14, 'd':15, "L":15, "Ú":15, "M":15, "E":15, "Š":15, "other":36}),
            (37, {"eps": 1})
            ]

hittile_vowels = [
    (1, {"a":2, "e":2, "i":2, "u":2, "other":3}),
    (2, {"-":4, "other":5}),
    (3, {"-":6, "other":5}),
    (4, {"a":7, "e":7, "i":7, "u":7, "other":5}),
    (5, {"-":6, "other":5}),
    (6, {"a":7, "e":7, "i":7, "u":7, "other":5}),
    (7, {"-":8, "other":5}),
    (8, {"a":7, "e":7, "i":7, "u":7, "other":5})
]

word = [["","", []]]
index = []
toRemove = []
canRemove = -1


def appendSymbol(symbol, lang):
    if word[-1][1] == "":
        word[-1][1] = lang
    if word[-1][1] == lang:
        if symbol not in index:
            index.append(symbol)
            word[-1][0] += string[symbol]
            word[-1][2].append(symbol)
    else:
        if symbol not in index:
            index.append(symbol)
            word.append([string[symbol], lang, [symbol]])


def handle_state(cur_state, cur_symbol):
        if cur_state == 1 and word[-1][0] == "YES":
            word[-1][0] = ""
        elif cur_state == 1 and word[-1][0] == "NO":
            del word[-1]
        if cur_state == 1 and string[cur_symbol] == "-":
            if cur_symbol not in index:
                index.append(cur_symbol)
                word[-1][0] += string[cur_symbol]
                word[-1][2].append(cur_symbol)
        if cur_state == 2:
            appendSymbol(cur_symbol, "shumer")
        if cur_state == 5 and string[cur_symbol] == "-":
            if cur_symbol not in index:
                index.append(cur_symbol)
                word[-1][0] += string[cur_symbol]
                word[-1][2].append(cur_symbol)
        if cur_state == 6:
            appendSymbol(cur_symbol, "hittite")
        if cur_state == 7:
            appendSymbol(cur_symbol, "akkad")
        if cur_state == 14 and string[cur_symbol] == "-":
            if cur_symbol not in index:
                index.append(cur_symbol)
                word[-1][0] += string[cur_symbol]
                word[-1][2].append(cur_symbol)
        if cur_state == 15:
            if word[-1][0] == "YES" or word[-1][0] == "NO":
                del word[-1]
            elif word[-1][1] != "":
                word.append(["", "", []])
            if string[cur_symbol] != "d":
                appendSymbol(cur_symbol, "shumer")
            else:
                appendSymbol(cur_symbol, "hittite")
            word.append(["YES", "", []])
        if cur_state == 21 and word[-1][1] != "":
            word.append(["", "", []])
        if cur_state == 22 and word[-1][1] != "":
            word.append(["", "", []])
        if cur_state == 23 and word[-1][1] != "":
            word.append(["", "", []])
        if cur_state == 36:
            toRemove.append(cur_symbol)
            if word[-1][0] != "YES" and word[-1][0] != "NO":
                word.append(["NO", "", []])
        if cur_state == 37 and string[cur_symbol] != '-':
            toRemove.append(cur_symbol)
        if cur_state == 37 and string[cur_symbol] == '-' and cur_symbol not in index:
            index.append(cur_symbol)
            word[-1][0] += string[cur_symbol]
            word[-1][2].append(cur_symbol)


def run_hitt(cur_word):
    cur_chars = []
    cur_state = 1
    cur_symbol = 0
    while cur_symbol < len(cur_word):
        if (cur_word[cur_symbol] == 'í'):
            cur_chars.append(['i'])
        elif (cur_word[cur_symbol] == 'á'):
            cur_chars.append(['a'])
        elif cur_word[cur_symbol] != '-':
            cur_chars.append([cur_word[cur_symbol]])
        cur_transitions = hittile_vowels[cur_state - 1][1]
        if cur_word[cur_symbol] in cur_transitions:
            cur_state = cur_transitions[cur_word[cur_symbol]]
            cur_symbol += 1
        elif 'other' in cur_transitions:
            cur_state = cur_transitions['other']
            cur_symbol += 1
        if cur_state == 4:
            cur_chars[-1].extend(["single", "start"])
        if cur_state == 8:
            cur_chars[-1].extend(["single", "middle"])
    if cur_state == 7:
        cur_chars[-1].extend(["single", "end"])

    new_chars = []
    for i in range(len(cur_chars)):
        if i > 0 and cur_chars[i][0] in ['a', 'e', 'u'] and cur_chars[i-1][0] == cur_chars[i][0] and len(cur_chars[i-1]) == 1 and len(cur_chars[i]) == 1:
            continue
        new_chars.append(cur_chars[i])

    cur_chars = new_chars
    new_chars = []
    i = 0
    while i < len(cur_chars):
        if cur_chars[i][0] == 's':
            cur_chars[i][0] = 'š'
        if cur_chars[i][0] == 'h':
            cur_chars[i][0] = 'ḫ'
        if i > 0 and i < len(cur_chars) - 1 and cur_chars[i][0] == 'i' and cur_chars[i-1][0] in ['a', 'e', 'i', 'u'] and cur_chars[i+1][0] in ['a', 'e', 'i', 'u']:
            cur_chars[i][0] = 'y'
        if len(cur_word) < 2:
            new_chars.append(cur_chars[i])
            i += 1
        elif i < len(cur_chars) - 2 and cur_chars[i][0] == 'a' and cur_chars[i+1][0] == 'a' and cur_chars[i+2][0] == 'a':
            new_chars.append(['ā'])
            i += 3
        elif i < len(cur_chars) - 2 and cur_chars[i][0] == 'e' and cur_chars[i+1][0] == 'e' and cur_chars[i+2][0] == 'e':
            new_chars.append(['ē'])
            i += 3
        elif i < len(cur_chars) - 2 and cur_chars[i][0] == 'i' and cur_chars[i+1][0] == 'i' and cur_chars[i+2][0] == 'i':
            new_chars.append(['ī'])
            i += 3
        elif i < len(cur_chars) - 2 and cur_chars[i][0] == 'u' and cur_chars[i+1][0] == 'u' and cur_chars[i+2][0] == 'u':
            new_chars.append(['ū'])
            i += 3
        elif i < len(cur_chars) - 1 and cur_chars[i][0] == 'a' and cur_chars[i+1][0] == 'a' and len(cur_chars[i]) + len(cur_chars[i + 1]) > 2:
            new_chars.append(['ā'])
            i += 2
        elif i < len(cur_chars) - 1 and cur_chars[i][0] == 'e' and cur_chars[i+1][0] == 'e' and len(cur_chars[i]) + len(cur_chars[i + 1]) > 2:
            new_chars.append(['ē'])
            i += 2
        elif i < len(cur_chars) - 1 and cur_chars[i][0] == 'i' and cur_chars[i+1][0] == 'i' and len(cur_chars[i]) + len(cur_chars[i + 1]) > 2:
            new_chars.append(['ī'])
            i += 2
        elif i < len(cur_chars) - 1 and cur_chars[i][0] == 'u' and cur_chars[i+1][0] == 'u' and len(cur_chars[i]) + len(cur_chars[i + 1]) > 2:
            new_chars.append(['ū'])
            i += 2
        else:
            new_chars.append(cur_chars[i])
            i += 1

    new_string = ""
    for c in new_chars:
        new_string += c[0]
    return new_string


if __name__ == "__main__":
    cur_state = 1
    cur_symbol = 0

    handle_state(cur_state, cur_symbol)

    while cur_symbol < len(string):
        cur_transitions = automata[cur_state-1][1]
        if 'eps' in cur_transitions:
            cur_state = cur_transitions['eps']
            handle_state(cur_state, cur_symbol)
        elif string[cur_symbol] in cur_transitions:
            cur_state = cur_transitions[string[cur_symbol]]
            handle_state(cur_state, cur_symbol)
            cur_symbol += 1
        elif 'other' in cur_transitions:
            cur_state = cur_transitions['other']
            handle_state(cur_state, cur_symbol)
            cur_symbol += 1

    if word[-1][0] == "":
        del word[-1]

    res = ""

    wordsStarts = {}
    for i in range(len(word)):
        wordsStarts[word[i][2][0]] = i

    new_words = []
    for w in word:
        if w[1] != 'hittite':
            new_words.append(w[0])
        else:
            cur_string = run_hitt(w[0])
            new_words.append(cur_string)

    i = 0
    while i < len(string):
        if i in toRemove:
            i = i + 1
            continue
        elif i in wordsStarts:
            res += new_words[wordsStarts[i]]
            i = word[wordsStarts[i]][2][-1] + 1
        else:
            res += string[i]
            i = i + 1

    f = open("res.html", "w", encoding="utf-8")
    f.write(res)
    f.close()
