from copy import deepcopy

with open('11-input.txt') as f:
    data = f.read().strip()
monkey, OP, DIV, TRUE, FALSE = [], [], [], [], []


def parse(a, b):
    return a.append(int(b.split()[-1]))

for line in data.split('\n\n'):
    id_, items, op, test, true, false = line.split('\n')
    monkey.append([int(i) for i in items.split(':')[1].split(',')])
    words = op.split()
    op = ''.join(words[-3:])
    OP.append(lambda old,op=op:eval(op))     
    parse(DIV, test)
    parse(TRUE, true)
    parse(FALSE, false)

START = deepcopy(monkey)


lcm = 1
for x in DIV:
    lcm *= x
print(lcm)

for part in [1,2]:
    C = [0] * len(monkey)
    monkey = deepcopy(START)
    for t in range(20 if part==1 else 10000):
        for i in range(len(monkey)):
            for item in monkey[i]:
                C[i] += 1
                item = OP[i](item)
                
                if part == 2:
                    item %= lcm
                
                if part == 1:
                    item = (item // 3)
                
                if item % DIV[i] == 0:
                    monkey[TRUE[i]].append(item)
                
                else:
                    monkey[FALSE[i]].append(item)
            monkey[i] = []
    print(sorted(C)[-1] * sorted(C)[-2])
