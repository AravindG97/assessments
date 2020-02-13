a="[({})]"
inputt="[](){"
dic,li_a,li_b={},[],[]
for x in a:
    li_a.append(x)
for x in inputt:
    li_b.append(x)
flag=True
try:
    for x in range(len(a)):
        dic[ord(a[x])]=ord(inputt[x])
    for x,y in dic.items():
        if x==y:
            pass
        else:
            flag=False
    if flag==True:
        print("true")
    else:
        print("false")

except:
    for x in li_a:
        if x not in li_b:
            print(x)