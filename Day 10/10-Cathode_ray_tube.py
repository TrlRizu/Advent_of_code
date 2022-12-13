with open('10-input.txt') as f:
    lines = [x for x in f.read().strip().split('\n')]

X,count,c = 1,0, [20, 60, 100, 140, 180, 220]
p1 = 0
p2 = [[None] * 40 for _ in range(6)]

def draw(count, X):
    global p2
    _count = count-1
    a,b = _count//40, _count%40
    p2[a][b] = ('██' if abs(X-b) <= 1 else '  ')

for line in lines:
    cmd = line.strip().split()
    if cmd[0] == 'addx':
        count += 1
        draw(count,X)

        if count in c:
            p1 += X * count
        count += 1

        if count in c:
            p1 += X*count
        draw(count,X)
        X += int(cmd[1])    

    elif cmd[0] == 'noop':
        count += 1

        if count in c:
            p1 += X*count
        draw(count,X)

print(p1)

for r in range(6):
    print(''.join(p2[r]))

