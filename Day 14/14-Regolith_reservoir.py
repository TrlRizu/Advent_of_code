with open("14-input.txt") as f:
    lines = f.read().strip().split("\n")

sand_source = 500, 0
filled = set()

for line in lines:
    coords = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
    for (x1,y1), (x2,y2) in zip(coords, coords[1:]):
        x1, x2 = sorted([x1,x2])
        y1, y2 = sorted([y1,y2])  
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 +1):    
                filled.add((x1,y))
                filled.add((x, y1))
        
max_y = max([coord[1] for coord in filled])

def sim(pt):
    global filled
    x, y = 500, 0
    
    if pt == 1:
        while y <= max_y:
            if (x, y + 1) not in filled:
                y += 1
                continue
            if (x - 1, y + 1) not in filled:
                x -= 1
                y += 1
                continue
            if (x + 1, y + 1) not in filled:
                x += 1
                y += 1
                continue
            filled.add((x, y))
            return True
        return False
    
    if pt == 2:
        if (x, y) in filled:
            return (x, y)

        while y <= max_y:
            if (x, y + 1) not in filled:
                y += 1
                continue

            if (x - 1, y + 1) not in filled:
                x -= 1
                y += 1
                continue

            if (x + 1, y + 1) not in filled:
                x += 1
                y += 1
                continue
            break
        return (x, y)  

ans = 0
for p in [1,2]:
    while True:
        if p == 1:
            r = sim(1)
            if not r:
                break
            ans += 1
        if p == 2:
            x, y = sim(2)
            filled.add((x, y))
            ans += 1
            if (x, y) == (500, 0):
                break
    print(ans)