with open('15-input.txt') as f:
    data = f.read().strip().splitlines()

S = set()
B = set()
for line in data:
    sensor, beacon = line.split(': ')
    x, y = sensor.split(', ')
    sx = int(x.split(' ')[-1].split('=')[1])
    sy = int(y.split('=')[1])
    x1,y1 = beacon.split(', ')
    bx = int(x1.split(' ')[-1].split('=')[1])
    by = int(y1.split('=')[1])
    d = abs(sx-bx) + abs(sy-by)
    S.add((sx,sy,d))
    B.add((bx,by))

def part1(num, S):
    r = 0
    for x in range(int(-6e6), int(6e6)):
        k = True
        for (sx,sy,d) in S:
            md = abs(sx-x) + abs(sy-num)
            if md <= d:
                k = False
                break
        if not k:
            if (x, num) not in B:
                r += 1
    return r

def part2(S):
    def acc(x,y,S):
        for (sx,sy,d) in S:
            md = abs(x-sx)+abs(y-sy)
            if md<=d:
                return False
        return True
    k = False
    ckd = 0
    for (sx,sy,d) in S:
        for dx in range(d+2):
            dy = (d+1)-dx
            for cx,cy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                ckd += 1
                x = sx+(dx*cx)
                y = sy+(dy*cy)
                if not(0<=x<=4000000 and 0<=y<=4000000):
                    continue
                if acc(x,y,S) and (not k):
                    return x*4000000+y
                
print(part1(2000000, S))   
print(part2(S))