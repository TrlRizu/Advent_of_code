for l in open('1-data.in'):
    X = l.strip()

Q = []
for i in ('\n'.join(X)).split('\n\n'):
    q = 0
    for x in i.split('\n'):
        q += int(x)
    Q = sorted(Q.append(q))
   
#p1 
print(max(Q))
#p2
print(Q[-1]+Q[-2]+Q[-3])

