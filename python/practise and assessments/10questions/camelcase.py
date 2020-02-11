def camelcase(string):
    op=""
    for x in string:
        a=ord(x)
        if(a>=97 and a<=122):
            a=a-32
            op=op+chr(a)
        elif(a>=65 and a<=90):
            a=a+32
            op=op+chr(a)
        else:
            op=op+chr(a)

    print(op)
camelcase("Hi Hello How")