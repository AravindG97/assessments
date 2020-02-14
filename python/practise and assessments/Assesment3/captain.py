# a=5
# inputt="1236544253616532412514368431562"
a=int(input("enter the size of groups: "))
inputt=input("enter the room numbers: ")
length=len(inputt)
min_length=length-(a*(length//a))
li=[]
for x in inputt:
    if x not in li:
        li.append(x)
print(li)
for x in li:
    count=inputt.count(x)
    if count==min_length:
        print(x)