import re
a=int(input("enter the no of inputs: "))
li,op=[],[]
for x in range(a):
    li.append(input("enter the email: "))
for x in li:
    if re.match("[a-zA-Z0-9_-]{2,64}@[a-zA-Z0-9]{2,10}\.[a-zA-Z]{2,50}",x):
        op.append(x)
op.sort()
print(op)