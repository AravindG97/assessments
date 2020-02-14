a=int(input("enter the no of students: "))
li,dic,sum,values=[],{},0,0
for x in range(a):
    li.append(input("enter the data: "))
bb=input("enter the particular student: ")
for x in li:
    aa=x.split(" ")
    li1=[]
    for xx in range(1,len(aa)):
        li1.append(aa[xx])
    dic[aa[0]]=li1
print("As dictionary ",dic)
for x,y in dic.items():
    if x==bb:
        for values in y:
            sum=sum+int(values)
            average=sum/int(len(y))
print(average)
