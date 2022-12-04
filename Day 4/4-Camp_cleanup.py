with open('4-input.txt') as f:
    data = f.read().strip().split('\n')
    data = [duo.split(',') for duo in data]


#part 1
count1 = 0
count2 = 0

for pairs in data:
    firstelf = pairs[0].split('-')
    secondelf = pairs[1].split('-')

    range1 = set(range(int(firstelf[0]), int(firstelf[1]) + 1))
    range2 = set(range(int(secondelf[0]), int(secondelf[1]) + 1))

    if range1.issubset(range2) or range2.issubset(range1):
        count1 += 1
        
#part 2
    if len(range1 & range2) > 0:
        count2 += 1
