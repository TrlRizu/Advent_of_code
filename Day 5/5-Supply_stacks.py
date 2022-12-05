import sys

with open('5-input.txt') as f:
    data = f.read().strip()
    lines = [x for x in data.split('\n')]

S = []
for line in lines:
    if line == '':
        break
    sz = (len(line)+1)//4
    while len(S) < sz:
        S.append([])
    for i in range(len(S)):
        c = line[1+4*i]
        if c != ' ' and c.isalpha():
            S[i].append(c)
# print(S)
found = False
for command in lines:
    if command == '':
        found = True
        continue
    if not found:
        continue
    words = command.split()
    qty = int(words[1])
    from_ = int(words[3])-1
    to_ = int(words[5])-1
    MOVE = S[from_][:qty]
    S[from_] = S[from_][qty:]
    #part one
    # S[to_] = list(reversed(MOVE)) + S[to_] 
    #part two
    S[to_] = MOVE + S[to_]

print(''.join(s[0] for s in S if s))
