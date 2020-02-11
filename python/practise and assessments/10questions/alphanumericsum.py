import functools

def numericsum(a):
    b=list(filter(lambda x:x.isdigit(),a))
    c=functools.reduce(lambda x,y:int(x)+int(y),b)
    print(c)


string="12ada2w3443sad"
numericsum(string)
