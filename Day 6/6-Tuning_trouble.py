with open("6-input.txt") as f:
    d = f.read()

def sol(n):
    i = 0
    while True:
        if len(set(list(d[i:(i+n)]))) == n: return i+n; break          
        i+=1
#part 1
print(sol(4))
#part 2
print(sol(14))

#ORIGINAL
# with open("6-input.txt") as f:
#     d = f.read()

# #part 1
# for i in range(len(d)-4):
#     if i - 3 >= 0 and len(set([d[i+j] for j in range(4)])) == 4:
#         print(i+4)
#         break
# #part 2
# for i in range(len(d)-14):
#     if i - 13 >= 0 and len(set([d[i+j] for j in range(14)])) == 14:
#         print(i+14)
#         break

