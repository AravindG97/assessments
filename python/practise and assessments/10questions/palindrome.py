def palindrome(a):
    if a.isdigit():
        a=int(a)
        if(a<0):
            print("not a palindroe")
        else:
            temp = a
            rev = 0
            while (a > 0) :
                dig = a % 10
                rev = rev * 10 + dig
                a = a // 10
            if rev==temp:
                print("its palinddrome")
    else:
        temp=a[::-1]
        if temp==a:
            print("its palindrome")
        else:
            print("its not palindrome")
ip=input("enter: ")
palindrome(ip)
