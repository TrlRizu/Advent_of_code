with open('9-input.txt') as f:
    lines = [x for x in f.read().strip().split('\n')]

#Function that takes in 2 parameters -heads and tails coordinates
def move(H,T):
    y = (H[0]-T[0]) #measure the distance between the y-coords
    x = (H[1]-T[1]) #measure the distance between the x-coords
    # print("y: ",  y, "\n", "x: ",  x)
    # print("H: ", H, "\n")
    
    #If HEADS and TAILS are touching or within a square don't do anything
    if abs(y)<=1 and abs(x)<=1:
        pass
    #For part 2
    #it it's 2 squares in both x, y 
    #y-axis moves to be one square away, x-axis moves to be one square away (diagonal movement)
    elif abs(y)>=2 and abs(x)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1]-1 if T[1]<H[1] else H[1]+1)
    #If y-axis is 2 squares away
    #y-axis moves to be one square away, x-axis should remain to match (in short: y follows)
    elif abs(y)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1])
    #If x-axis is 2 squares away
    #y-axis should remain to match, x-axis moves to be one square away (in short: x follows)
    elif abs(x)>=2:
        T = (H[0], H[1]-1 if T[1]<H[1] else H[1]+1)
    return T

HEADS = (0,0) #Origin coords
TAILS = [(0,0) for _ in range(9)] #create 9 

#create a dictionary for movements by direction
DY = {'L': 0, 'U': -1, 'R': 0, 'D': 1} 
DX = {'L': -1, 'U': 0, 'R': 1, 'D': 0} 

p1 = set([TAILS[0]])
p2 = set([TAILS[8]])

for line in lines:
    dir,mvs = line.split() 
    mvs = int(mvs) 
    for _ in range(mvs):
    
        HEADS = (HEADS[0] + DY[dir], HEADS[1]+DX[dir]) #Update HEADS coords every movement
        TAILS[0] = move(HEADS, TAILS[0])  #Call move function and update the TAILS movement as it tries to follow HEADS
        for i in range(1, 9):
            TAILS[i] = move(TAILS[i-1], TAILS[i]) #Update the coords of knots and the TAILS
        p1.add(TAILS[0]) #only TAILS
        p2.add(TAILS[8]) #knots and Tails
print(len(p1))
print(len(p2))