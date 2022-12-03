score = 0
two_score = 0
for i in open('2-data.in'):
    data = i.strip().split('\n')
#part 1
    output = { 
        "A X" : 4, "A Y" : 8, "A Z" : 3,
        "B X" : 1, "B Y" : 5, "B Z" : 9,
        "C X" : 7, "C Y" : 2, "C Z" : 6  
    }   
    
    for line in data:
        score += output[line]
    
#part 2
    choose_output = { 
        "A X" : 3, "A Y" : 4, "A Z" : 8,
        "B X" : 1, "B Y" : 5, "B Z" : 9,
        "C X" : 2, "C Y" : 6, "C Z" : 7  
    }   

    for r in data:
        two_score += choose_output[r]
print(score)
print(two_score)