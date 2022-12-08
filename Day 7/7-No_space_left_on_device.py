from collections import defaultdict

data = open('7-input.txt').read().strip()
lines = [x for x in data.split('\n')]

size = defaultdict(int)
path = []
for line in lines:
    cmd = line.strip().split()
    # print(cmd)
    if cmd[1] == 'cd':
        if cmd[2] == '..':
            path.pop()
        else:
            path.append(cmd[2])
    elif cmd[1] == 'ls':
        continue
    elif cmd[0] == 'dir':
        continue
    else:
        num = int(cmd[0])
        # print(path)
        for i in range(len(path)+1):
            size['/'.join(path[:i])] += num

p1 = 0
p2 = 1000000000       
           
# unused = 70000000 - size['/']
# freeup = 30000000 - unused
for a,b in size.items():
    if b <= 100000:
        p1 += b
    if b >= 30000000 - (70000000 - size['/']):
        p2 = min(p2, b)
print(p1, p2)
