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


n = len(grid)
m = len(grid[0])
grid = np.array(grid)

p1 = 0
p2 = 0
for i in range(n):
    for j in range(m):
        h = grid[i,j]
        count = 1

        if j == 0 or np.amax(grid[i, :j]) < h:
            p1 += 1
        elif j == m-1 or np.amax(grid[i, (j+1):]) < h:
            p1 += 1
        elif i == 0 or np.amax(grid[:i, j]) < h:
            p1 += 1
        elif i == n-1 or np.amax(grid[(i+1):, j]) < h:
            p1 += 1

        for di, dj in DIR:
            ii, jj = i,j
            dist = 0
            ii += di
            jj += dj
            while (0 <= ii < n and 0 <= jj < m) and grid[ii, jj] < h:
                dist += 1
                ii += di
                jj += dj
                    
                if (0 <= ii < n and 0 <= jj < m) and grid[ii][jj] >= h:
                    dist += 1
               
            count *= dist
        p2 = max(p2, count)

print(p1, p2)

