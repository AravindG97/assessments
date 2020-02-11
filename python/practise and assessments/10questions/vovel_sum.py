def vovelsum(string):
    dic={"a":1,"e":2,"i":3,"o":4,"u":5}
    sum=0
    for x in string:
        for i,j in dic.items():
            if x==i:
                sum=sum+j
    print("the vovel sum is:",sum)

string="hello-vovel-sum"
vovelsum(string)