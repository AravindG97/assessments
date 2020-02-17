rangee=int(input("enter the range: "))
sum=0
for x in range(rangee):
    if(x%3==0):
        sum=sum+x

print("the sum is",sum)