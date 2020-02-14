a=int(input("enter the size: "))
for x in range(1,a+1):
    if x==1:
        print(x)
        pass
    else:
        a=""
        for y in range(1,x):
            a=a+str(y)
        print(a+str(x)+a[::-1])