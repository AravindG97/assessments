a=[1,2]
b=[3,4]
li=[]
for x in range(len(a)):
    for y in range(len(b)):
        op=(a[x],b[y])
        li.append(op)
print(li)