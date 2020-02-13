def count(string):
    b=[]
    a=""
    for x in string:
        if x not in b:
            b.append(x)
    for x in b:
        a=a+x+str(string.count(x))
    print(a)
count(input("enter the string: "))