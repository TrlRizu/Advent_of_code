import numpy as np

with open('8-input.txt', 'r') as f:
    data = f.read().strip().split()
grid = [list(map(int, list(a))) for a in data]




r = len(grid) #row
c = len(grid[0]) #column

#convert the data into a numpy array
grid = np.array(grid) 
#Output:
"""
[[3 0 1 ... 1 2 3]
 [2 1 2 ... 1 1 1]
 [2 0 1 ... 2 3 1]
 ...
 [0 1 2 ... 2 0 3]
 [1 3 2 ... 1 1 2]
 [0 1 1 ... 3 0 2]]
"""

#For part2
DIR = [
        (0,1),   #right
        (0,-1),  #left
        (-1,0),  #down
        (1,0)    #up
    ]

p1 = 0
p2 = 0

#Iterate through the rows and columns
for i in range(r):
    for j in range(c):
        h = grid[i,j]
        count = 1

        """"        
        If the tree is on the left edge; increment
        Othewise, scan left; take the maximum value of a tree west, the current tree
        If max tree height is less than the current tree height; increment
        
        30373
        25512
        65332
        33549 --> middle 5
        35390

        For e.g middle 5:
            Middle 5 is not on the edge, hence scan the left side.
            Take the maximum value on the left side (3), and compare it with the current height (5)
            If max val is lesser than current height; increment p1

        """
        if j == 0 or np.amax(grid[i, :j]) < h:
            p1 += 1
        #Scan RIGHT-SIDE (EAST)
        elif j == c-1 or np.amax(grid[i, (j+1):]) < h:
            p1 += 1
        #Scan UPWARDS (NORTH)
        elif i == 0 or np.amax(grid[:i, j]) < h:
            p1 += 1
        #Scan DOWNWARDS (SOUTH)
        elif i == r-1 or np.amax(grid[(i+1):, j]) < h:
            p1 += 1

#part 2
        #Scan in 4 directions
        for di, dj in DIR:
            ii, jj = i + di, j + dj #Start at coords (i,j), but as we iterate, update it according to the steps taken
            #print("II: ", ii, "\n", "JJ: ", jj)
            
            dist = 0 #Initialize distance 
            
            #Iterate through the grid, whilst staying within the columns (c) and rows (r)
            while (0 <= ii < r and 0 <= jj < c) and grid[ii, jj] < h:
                """
                30373
                25512
                65332
                33549 --> middle 5
                35390
                
                Calculating distance to the left of middle 5
                Moved a distance of 3:
                    335 -->middle 5
                    33 --> distance += 1
                    3 --> distance += 1 (distance = 2)
                    Outside of the grid as the last digit 3 is counted as a distance --> distance += 1 (distance = 3)  
                """
                dist += 1
                ii += di
                jj += dj

                """
                30373
                25512
                65332
                33549 --> middle 5
                35390

                If the iteration stops within the grid and the tree is taller than the current tree
                Include it in the count; increment distance by 1

                """                
                if (0 <= ii < r and 0 <= jj < c) and grid[ii][jj] >= h:
                    dist += 1
            #Multiply the distance by the count 
            count *= dist
        p2 = max(p2, count)
print(p1, p2) 




