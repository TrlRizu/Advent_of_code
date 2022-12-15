with open("14-input.txt") as f:
    lines = f.read().strip().split("\n")

filled = set()

for line in lines:
    #Split data by the arrows, and split the new data by commas and map that as integers
    coords = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
    #unpack the values as pairs of integers 
    for (x1,y1), (x2,y2) in zip(coords, coords[1:]):
        #sort the coords in increasing order
        x1, x2 = sorted([x1,x2]) 
        y1, y2 = sorted([y1,y2]) 
        #loop through the values of x and y; add 1 to include the end point; this becomes a rectangle but since either x's and y's are equal, it becomes a line
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 +1):    
                filled.add((x1,y)) #take the current value of x
                filled.add((x, y1)) #take the current value of y

#find the maximum y coordinate of the rocks; layer of the bottom rock
ymax = max([coord[1] for coord in filled])

def sim(pt):
    global filled
    x, y = 500, 0
    
    if pt == 1:
        #keep falling as long as the sand stays above the maximum y coordinate
        while y <= ymax:
            #fall down by increasing y-coordinate, check if the downward location is filled
            if (x, y + 1) not in filled:
                y += 1  #if it's not filled add 1
                continue #keep looping
            #if it can't fall down, move to the left, decrease x-coordinate and increasing y-coord by 1
            if (x - 1, y + 1) not in filled:
                x -= 1
                y += 1
                continue
            #if we can't move to the left, move to the right, increase x and y coordinates
            if (x + 1, y + 1) not in filled:
                x += 1
                y += 1
                continue
            #if all the places are filled, stop
            filled.add((x, y))
            return True #return true if the sand stops moving
        return False #return false if the sand never stops falling
    
    if pt == 2:
        #continue falling even after the final line of sand
        if (x, y) in filled:
            return (x, y)

        while y <= ymax:
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
            #Everything is filled, sand has come to rest
            break
        return (x, y)  #returnt the location of the sand

ans = 0
for p in [1,2]:
    while True:
        if p == 1:
            r = sim(1) 
            if not r: #If r is false, then that sand is falling forever
                break #stop the loop
            ans += 1 #If that sand has stopped, count that
        if p == 2:
            x, y = sim(2)
            filled.add((x, y))
            ans += 1
            if (x, y) == (500, 0): #if the sand had blocked the source, stop the loop
                break
    print(ans)