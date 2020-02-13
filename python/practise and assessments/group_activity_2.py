import re
class Person:
    def __init__(self,person_name,person_age):
        self.person_name=person_name
        self.person_age=person_age
    def show_age(self):
        return self.person_age

class Student(Person):
    def __init__(self,type="",person_name="",person_age=0):
        self.type=type
        Person.__init__(self,person_name,person_age)
    def determine_hostelite(self):
        b=self.type.lower()

        if re.match(r"\bhos\w+",b) and re.match("[a-zA-Z]+",b):
            print("awww u r in hostel")
        elif re.match(r"\w+lite\b",b) and re.match(r"\w+lit\B",b):
            print("try to come early")

try:
    listt=[]

    # obj1=Student()
    # obj2=Student()
    # obj3=Student()
    obj3=[]
    # obj=['obj1','obj2','obj3']
    f = open("C:\\Users\\akshatha.a.suresh\\PycharmProjects\\practice\\reading_file", "r")
    l=f.read().splitlines()
    print(l)
    for i in l:
        c=i.split(" ")
        listt.append(c)
        # print(c)
    print(listt)
    for x in range(len(listt)):
        name=listt[x][0]
        age=listt[x][1]
        # id+str(x)=k[3]
        type=listt[x][2]

        # obj[x]=Student(type,name,age)
        obj3.append(Student(type,name,age))
        # print(obj[x].show_age())
        print(obj3[x].show_age())
        obj3[x].determine_hostelite()





except FileNotFoundError:
    print("Please Enter a valid path")
