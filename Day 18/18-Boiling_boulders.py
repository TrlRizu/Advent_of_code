from collections import deque
with open('18-input.txt') as f:
    lines = [x for x in f.read().strip().split('\n')]

C = set()
for line in lines:
    x,y,z = line.split(',')
    x,y,z = int(x),int(y),int(z)
    C.add((x,y,z))

def sol(p):
    def offbounds(x,y,z,p):
        vis = set()
        Q = deque([(x,y,z)])
        while Q:
            x,y,z = Q.popleft()
            if (x,y,z) in C:
                continue
            if (x,y,z) in vis:
                continue
            vis.add((x,y,z))
            if len(vis) > (0 if p==1 else 5000):
                return True
            for d in [-1,1]:
                Q.append((x+1, y, z))
                Q.append((x-1, y, z))
                Q.append((x, y+1, z))
                Q.append((x, y-1, z))
                Q.append((x, y, z+1))
                Q.append((x, y, z-1))
        return False
    
    res = 0
    for (x,y,z) in C:
        if offbounds(x+1,y,z,p):
            res += 1
        if offbounds(x-1,y,z,p):
            res += 1
        if offbounds(x,y+1,z,p):
            res += 1
        if offbounds(x,y-1,z,p):
            res += 1
        if offbounds(x,y,z+1,p):
            res += 1
        if offbounds(x,y,z-1,p):
            res += 1
    return res
print(sol(1))
print(sol(2))

    
