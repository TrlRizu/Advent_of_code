from collections import deque
with open('12-input.txt') as f:
    lines = [x for x in f.read().strip().split('\n')]


#Create a grid depending on the data's length and width
G = [list(line) for line in lines] 
R = len(G) #rows
C = len(G[0]) #columns
E = [[0 for _ in range(C)] for _ in range(R)]
DIR = [(-1,0),(0,1),(1,0),(0,-1)]


for r in range(R):
    for c in range(C):
        if G[r][c]=='S': #Start, give it the value 1 similar to it being the first letter of the alphabet
            E[r][c] = 1 
        elif G[r][c] == 'E': #End, give it the value 26 similar to it being the last letter of the alphabet
            E[r][c] = 26
        else:
            E[r][c] = ord(G[r][c])-ord('a')+1 #Number the other alphabets by taking their ascii value and subtracting it with the ascii 'a' + 1

#Breadth first search algorithm
def bfs(part):
    Q = deque() #create an empty queue
    for r in range(R): 
        for c in range(C):
            if (part==1 and G[r][c]=='S') or (part==2 and E[r][c] == 1):
                Q.append(((r,c), 0))
    
    visited = set()
    while Q:
        (r,c),d = Q.popleft() #Take out the node from the queue when it is visited
        if (r,c) in visited:
            continue 
        visited.add((r,c)) #add the nodes to the visited
        if G[r][c]=='E':
            return d
        for dr,dc in DIR: #search in all four directions: up, down, left, right
            rr = r+dr #add r to the current differential, new possible step
            cc = c+dc #similar with r
            if 0<=rr<R and 0<=cc<C and E[rr][cc]<=1+E[r][c]:
                Q.append(((rr,cc),d+1))
print(bfs(1)) #part 1
print(bfs(2)) #part 2