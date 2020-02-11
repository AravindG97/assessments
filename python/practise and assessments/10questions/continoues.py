s = "abcdefgabcijkmxtyabcdefghijkz"
count = 0
temp = 0
liss = ""
listt = []
dic = {}
for x in range (len (s)) :
    if count == 0 :
        temp = ord (s[x])
        # print("aa",s[x])
        # count=1
        count = count + 1
        liss += s[x]
        continue
    else :
        if temp + 1 == ord (s[x]) :
            count += 1
            # print(s[x])
            temp = ord (s[x])
            liss += s[x]

        else :

            # print(liss)
            # print("bb",s[x])
            # print("bbb",count)
            dic[liss] = count
            listt.append (count)
            liss = ""
            liss += s[x]
            count = 1
            temp = ord (s[x])

# print (count)
# print (listt)
# print (dic)
listt=sorted(listt,reverse=True)
# print(listt)
for i,j in dic.items():
    if listt[0]==j:
        print(j,i)

