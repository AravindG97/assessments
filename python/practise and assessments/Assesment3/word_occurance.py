a=int(input("enter the no of words: "))
li=[]
unique=[]
for x in range(a):
    li.append(input("enter: "))

for x in li:
    if x not in unique:
        unique.append(x)
print(len(unique))
for x in unique:
    print(li.count(x),end=" ")