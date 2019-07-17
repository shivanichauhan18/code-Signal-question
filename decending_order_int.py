def makeDeceningOrder(input):
    v=str(input)
    b=list(map(int,v))
    i=1
    str_a=""
    while i<=len(b):
        str_a=str_a+str(b[-i])
        i=i+1
    return str_a
print makeDeceningOrder(21445)