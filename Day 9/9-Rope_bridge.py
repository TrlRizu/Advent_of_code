with open('9-input.txt') as f:
    lines = [x for x in f.read().strip().split('\n')]

def adjust(H,T):
    y = (H[0]-T[0])
    x = (H[1]-T[1])
    
    if abs(y)<=1 and abs(x)<=1:
        pass  
    elif abs(y)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1])
    elif abs(x)>=2:
        T = (H[0], H[1]-1 if T[1]<H[1] else H[1]+1)
    elif abs(y)>=2 and abs(x)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1]-1 if T[1]<H[1] else H[1]+1)
    
    return T

HEADS = (0,0)
TAILS = [(0,0) for _ in range(9)]
DR = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
DC = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
p1 = set([TAILS[0]])
p2 = set([TAILS[8]])

for line in lines:
    dir,mvs = line.split()
    mvs = int(mvs)
    for _ in range(mvs):
        HEADS = (HEADS[0] + DR[dir], HEADS[1]+DC[dir])
        TAILS[0] = adjust(HEADS, TAILS[0])
        for i in range(1, 9):
            TAILS[i] = adjust(TAILS[i-1], TAILS[i])
        p1.add(TAILS[0])
        p2.add(TAILS[8])
print(len(p1))
print(len(p2))