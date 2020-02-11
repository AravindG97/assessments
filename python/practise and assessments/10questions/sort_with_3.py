def sort_with_3(lis):
    print("input",lis)
    dic={}
    sor=[]
    for x in lis:
        sor.append(x[2])
        dic[x]=x[2]
    sor.sort(reverse=True)
    lis.clear()
    for x in sor:
        for i,j in dic.items():
            if x==j:
                lis.append(i)
    print("output",lis)


a=["abcd","qwerty","zxgvb"]
sort_with_3(a)