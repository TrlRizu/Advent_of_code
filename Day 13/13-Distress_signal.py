from functools import cmp_to_key
with open('13-input.txt') as f:
    data = f.read().strip()


def cmp(l,r):
    if isinstance(l, int) and isinstance(r,int):
        if l < r:
            return -1
        elif l == r:
            return 0
        else:
            return 1
    elif isinstance(l, list) and isinstance(r, list):
        i = 0
        while i<len(l) and i<len(r):
            c = cmp(l[i], r[i])
            if c==-1:
                return -1
            if c==1:
                return 1
            i += 1
        if i==len(l) and i<len(r):
            return -1
        elif i==len(r) and i<len(l):
            return 1
        else:
            return 0
    elif isinstance(l, int) and isinstance(r, list):
        return cmp([l], r)
    else:
        return cmp(l, [r])

packets = []
p1 = 0
for i,group in enumerate(data.split('\n\n')):
    l,r = group.split('\n')
    l = eval(l)
    r = eval(r)
    packets.append(l)
    packets.append(r)
    if cmp(l, r)==-1:
        p1 += 1+i
print(p1)

packets.append([[2]])
packets.append([[6]])
packets = sorted(packets, key=cmp_to_key(lambda l,r: cmp(l,r)))
p2 = 1
for i,p in enumerate(packets):
    if p ==[[2]] or p == [[6]]:
        p2 *= i+1
print(p2)