from copy import deepcopy

with open('11-input.txt') as f:
    data = f.read().strip()
#Create lists for the inputs
monkey, OP, DIV, TRUE, FALSE = [], [], [], [], [] 

def parse(a, b):
    return a.append(int(b.split()[-1])) #parse the data, return the a list of integers which are the last element of the sentence

for line in data.split('\n\n'):
    id_, items, op, test, true, false = line.split('\n') #split the data and assign them to their values
    #append the starting items to the list as a list of integers 
    monkey.append([int(i) for i in items.split(':')[1].split(',')]) 
    words = op.split() 
    op = ''.join(words[-3:]) #take the last 3 words of the operation "new = old * 11"
    OP.append(lambda old,op=op:eval(op)) # the last 3 words of the input are a valid python function of the single variable "old"
    parse(DIV, test) 
    parse(TRUE, true)
    parse(FALSE, false)

M = deepcopy(monkey) #copy the list for part 2

#FROM PYDIS:
#mod trick
# any number that is divisible by 7, is also divisible by 3*7 (or smaller than 3*7) seeing as how you don't care what the number is, 
# if your tests are "is it a multiple of 7" you can also take the mod of that, number % 21, 
# first and it'll still have the same result for "is it a multiple of 7"

mod = 1
for x in DIV: #go through all the numbers in DIV, which are actually prime numbers: 2,3,5,7,11,13,17,19
    mod *= x #2*3*5*7*11*13*17*19 

for part in [1,2]:
    C = [0] * len(M) #create a list containing the amount of items iterated by each monkey
    monkey = deepcopy(monkey)
    for t in range(20 if part==1 else 10000):
        for i in range(len(monkey)):
            for item in monkey[i]:
                C[i] += 1 #increment the list as each monkey iterates through the object
                item = OP[i](item)
                
                if part == 2:
                    item %= mod
    
                if part == 1:
                    item = (item // 3) #worry level decrease (instructions)
                
                if item % DIV[i] == 0:
                    monkey[TRUE[i]].append(item) #if the condiiton is true, append it to the instructed monkey
                
                else:
                    monkey[FALSE[i]].append(item) #if the condiiton is false, append it to the instructed monkey
            monkey[i] = []
    print(sorted(C)[-1] * sorted(C)[-2]) #print the 2 highest digits multiplied together










