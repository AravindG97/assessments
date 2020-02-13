dic={"{":"}","[":"]","(":")"}
ip="[]{()}[{"
lio=[]
lic=[]
for i in ip:
    for x,y in dic.items():
        if x==i:
            lio.append(i)
        elif y==i:
            lic.append(i)
temp=lic
for x in range(len(temp)):
    for i,j in dic.items():
        if i in lio and j in lic:
            lio.remove(i)
            lic.remove(j)
if len(lic)==0 and len(lio)==0:
    print("true")
elif len(lic)!=0 and len(lio)!=0:
    print ("false,the missing are"+str(" ".join(lio))+str(" ".join(lic)))
elif len(lio)==0:
    print ("false,the missing are"+str(" ".join(lic)))
else:
    print ("false,the missing are"+str(" ".join(lio)))