string = "<i>ma-a-an</i> <sup>d</sup>UTU-<i>ŠI-ma </i>"

automata = [(1, {"-":1, " ":1,"U":2, "T":2,"<":3}),(2, {"eps":1}),
            (3, {"i":4, "s":11}),
            (4, {">":5}),(5, {"-":5, " ":5, "m":6, "a":6, "n":6, "Š":7, "I":7,"<":8}),(6, {"eps":5}), (7, {"eps":5}),
            (8, {'/':9}), (9, {'i':10}), (10, {'>':1}),
            (11, {'u':12}), (12, {'p':13}), (13, {'>':14}),
            (14, {'d':15, "<":16}), (15, {"eps":14}), (16, {'/':17}), (17, {'s':18}), (18, {'u':19}), (19, {'p':20}), (20, {'>':1})]

hit = []
shum = []
akk = []

def handle_state(cur_state, cur_symbol):
        if cur_state == 1:
            pass
        if cur_state == 2:
            shum.append(cur_symbol)
        if cur_state == 6:
            hit.append(cur_symbol)
        if cur_state == 7:
            akk.append(cur_symbol)
        if cur_state == 15:
            hit.append(cur_symbol)

cur_state = 1
cur_symbol = 0

handle_state(cur_state, string[cur_symbol])

while cur_symbol < len(string):
    cur_transitions = automata[cur_state-1][1]
    if 'eps' in cur_transitions:
        cur_state = cur_transitions['eps']
        handle_state(cur_state, string[cur_symbol])
    else:
        cur_state = int(cur_transitions.get(string[cur_symbol]))
        handle_state(cur_state, string[cur_symbol])
        cur_symbol += 1

print (hit)
print (akk)
print (shum)

