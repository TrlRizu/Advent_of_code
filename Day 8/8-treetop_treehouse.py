import numpy as np

with open('8-input.txt', 'r') as f:
    data = f.read().strip().split()
    
grid = [list(map(int, list(a))) for a in data]
DIR = [
        (0,1),        
        (0,-1),
        (-1,0),
        (1,0)      
    ]

height = len(lines)
width = len(lines[0])

p1 = 0
for y in range(height):
    for c in range(width):
        vis = False
        for (dr,dc) in DIR:
            rr = y
            cc = c
            ok = True
            while True:
                rr += dr
                cc += dc
                if not (0<=rr<height and 0<=cc<width):
                    break
                if lines[rr][cc] >= lines[y][c]:
                    ok = False
            if ok:
                vis = True
        if vis:
            p1 += 1
# print(p1)

p2 = 0
for r in range(height):
    for c in range(width):
        score = 1
        for (dr,dc) in DIR:
            dist = 1
            rr = r+dr
            cc = c+dc
            while True:
                if not (0<=rr<height and 0<=cc<width):
                    dist -= 1
                    break
                if lines[rr][cc]>=lines[r][c]:
                    break
                dist += 1
                rr += dr
                cc += dc
            score *= dist
        p2 = max(p2, score)
print(p2)


