import math
class point:

    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def mid(self,x,y):
        self.aa=(x.a+y.a)/2
        self.bb=(x.b+y.b)/2
        return self
    def mid1(self,x,y):
        aa=(x.a+y.a)/2
        bb=(x.b+y.b)/2
        return aa,bb

    def distfromorigin(self):
        return math.sqrt((self.a)**2+(self.b)**2)
    def dis_between_twopoints(self,i,j):
        return math.sqrt((j.a-i.a)**2+(j.b-i.b)**2)


p1=point(4,5)
p2=point(7,9)
p3=point()
d=p3.mid(p1,p2)
a,b=p3.mid1(p1,p2)
print(p1.distfromorigin())
print(p3.dis_between_twopoints(p1,p2))
print(d.aa,d.bb)
print(a,b)