string = open("syllab.html", "r", encoding="utf-8")
string = string.read()

automata = [(1, {"other":1, "U":2, "Ú":2, "T":2, "K":2, "R":2, "É":2, "I":2, "N":2, "<":3, " ":21}),
            (2, {"eps":1}),
            (3, {"i":4, "s":11, "other":20}),
            (4, {">":22, "other":20}),
            (5, {" ":22, "\n":22, "other":5, "m":6, "a":6, "n":6, "k":6, "u":6, "w":6, "p":6, "í":6, "š":6,
                "i":6, "l":6, "ḫ":6, "z":6, "d":6, "e":6, "t":6, "r":6, "á":6, "Š":7, "I":7, "A":7, "<":8}),
            (6, {"eps":5}),
            (7, {"eps":5}),
            (8, {'/':9}),
            (9, {'i':10}),
            (10, {'>':21}),
            (11, {'u':12, 'other':20}),
            (12, {'p':13, 'other':20}),
            (13, {'>':23, 'other':20}),
            (14, {" ":23, "\n":23, "other":14, 'd':15, "L":15, "Ú":15, "M":15, "E":15, "Š":15, "<":24}),
            (15, {"eps":14}),
            (16, {'s':17, "other":24}),
            (17, {'u':18, "other":24}),
            (18, {'p':19}),
            (19, {'>':1}),
            (20, {">":21, "other":20}),
            (21, {"eps":1}),
            (22, {"eps":5}),
            (23, {"eps":14}),
            (24, {">":23, "other":24, "/":16})]

word = [["",""]]
index = []

def appendSymbol(symbol, lang):
    index.append(symbol)
    if word[len(word) - 1][1] == "":
        word[len(word) - 1][1] = lang
    if word[len(word) - 1][1] == lang:
        word[len(word) - 1][0] += string[symbol]
    else:
        word.append([string[symbol], lang])

def handle_state(cur_state, cur_symbol):
        if cur_state == 1 and string[cur_symbol] == "-":
            if cur_symbol not in index:
                index.append(cur_symbol)
                word[len(word) - 1][0] += string[cur_symbol]
        if cur_state == 2:
            appendSymbol(cur_symbol, "shumer")
        if cur_state == 5 and string[cur_symbol] == "-":
            if cur_symbol not in index:
                index.append(cur_symbol)
                word[len(word) - 1][0] += string[cur_symbol]
        if cur_state == 6:
            appendSymbol(cur_symbol, "hittite")
        if cur_state == 7:
            appendSymbol(cur_symbol, "akkad")
        if cur_state == 14 and string[cur_symbol] == "-":
            if cur_symbol not in index:
                index.append(cur_symbol)
                word[len(word) - 1][0] += string[cur_symbol]
        if cur_state == 15 and string[cur_symbol] != "d":
            appendSymbol(cur_symbol, "shumer")
        if cur_state == 15 and string[cur_symbol] == "d":
            appendSymbol(cur_symbol, "hittite")
        if cur_state == 22 and word[len( word) - 1][0] != "":
            word.append(["", ""])
        if cur_state == 23 and word[len( word) - 1][0] != "":
            word.append(["", ""])
        if cur_state == 24 and word[len( word) - 1][0] != "":
            word.append(["", ""])

cur_state = 1
cur_symbol = 0

handle_state(cur_state, cur_symbol)

while cur_symbol < len(string):
    cur_transitions = automata[cur_state-1][1]
    if 'eps' in cur_transitions:
        cur_state = cur_transitions['eps']
        handle_state(cur_state, cur_symbol)
    elif string[cur_symbol] in cur_transitions:
        cur_state = int(cur_transitions.get(string[cur_symbol]))
        handle_state(cur_state, cur_symbol)
        cur_symbol += 1
    elif 'other' in cur_transitions:
        cur_state = cur_transitions['other']
        handle_state(cur_state, cur_symbol)
        cur_symbol += 1

print(word)
