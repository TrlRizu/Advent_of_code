with open('3-data.txt', 'r') as f:
    data = f.read().split('\n')


#part 1
def p1():
    sum = 0
    for line in data:
        string_a = line[:len(line)//2]
        string_b = line[len(line)//2:]
        x = list(set(string_a)&set(string_b))[0]
    
        if x.isupper():
            sum += ord(x) - ord('A') + 27
        else:
            sum += ord(x) - ord('a') + 1
    return sum
print(p1())

#part 2
def p2():
    sum = 0
    for i in range(0, len(data), 3):
        x = list(set(data[i]) & set(data[i+1]) & set(data[i+2]))[0]
        
        if x.isupper():
            sum += ord(x) - ord('A') + 27
        else:
            sum += ord(x) - ord('a') + 1
    return sum
print(p2())


