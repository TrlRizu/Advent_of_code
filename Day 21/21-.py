from sympy import symbols, solve_linear
from sympy.parsing.sympy_parser import parse_expr

with open('21-input.txt') as f:
    data = f.read().strip().split('\n')

search = {}
humn = symbols("humn")

def calc(name, n):

    if name == "humn" and n == 2:
        return humn
    
    if isinstance(search[name], int):
        return search[name]
    
    
    expr = search[name]
    x = calc(expr[0], n)
    y = calc(expr[2], n)
    
    if n == 1:
        return int(eval(f"{x}{expr[1]}{y}"))
    else:
        return parse_expr(f"({x}){expr[1]}({y})")
    # print("parts: ", parts)    
    

for d in data:
    expr = d.split(" ")
    # print(expr)
    id_ = d.split()[0][:-1]    
    # print("monkey: ", id_)
    if len(expr) == 2:
        search[id_] = int(expr[1])
        # print("search: ", search[id_])
        # print(search[name])
    else:
        search[id_] = expr[1:]
#part 2
x = calc(search["root"][0], 2)
y = calc(search["root"][2], 2)

print(calc("root",1)) #part1
print(solve_linear(x,y)[1]) #part2