import math
li=[]
op=1
a=int(input("enter the no numbers: "))
for x in range(a):
    aa=int(input("numerator: "))                     #numerator input
    bb=int(input("denominator: "))                     #denominator input
    string=str(aa)+" "+str(bb)
    li.append(string)
for x in li:
    b=x.split(" ")
    op=op*(int(b[0])/int(b[1]))
sum=op.as_integer_ratio()

for x in sum:
    print(x,end=" ")
