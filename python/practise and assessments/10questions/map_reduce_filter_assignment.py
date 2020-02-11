import itertools
import functools
a=[1,2,3,4,5]
b=[1,2,3]
dic={1:"one",2:"two",3:"three"}
#1:
one=(lambda x:x+1)(2)
print(one)

#2:
""" x not defined error"""
two=(lambda x:x+1)
x(2)
print(two)

#3:
""" no error print utill available values"""
def pr(n,m):
    print(n*m)
    return n*m
print(list(map(pr,a,b)))

#4:
def asd(x,y):
    return pow(x,y)
print(list(map(pow,a,b)))
print(list(map(asd,a,b)))

#5:

five=list(map(lambda x:dic[x],dic))
print(five)
five1=list(map(lambda a,b:str(a)+" : "+dic[b],dic,dic))
print(five1)


#6:
six=list(map(lambda x: x if x%2==0 else "not divisible",a))
print(six)
six1=list(filter(lambda x:x%2==0,a))
print(six1)

#7:
seven=functools.reduce(lambda x,y:x+y,a)
print(seven)
seven1=itertools.accumulate(a,lambda x,y:x+y)
print(list(seven1))

