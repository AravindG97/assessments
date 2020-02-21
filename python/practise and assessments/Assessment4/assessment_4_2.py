class AgeError (Exception) :
    pass

class NameError(Exception):
    pass

try :
    print("welcome to the registration page".center(45,"-"))
    a=input("enter your full name: ")
    length=len(a.split(" "))
    if length==1:
        print(len(a.split(" ")))
        raise NameError("enter full name")
    b=int(input("enter your age: "))
    if b<=18:
        raise AgeError ("age limit violation")
    location=input("enter proper source destination to upload your files: ")
    file=open(location)
    print(file.read())



except AgeError as e :
    print(e)
except NameError as e:
    print(e)
except ValueError:
    print("enter the details accordingly")
except FileNotFoundError:
    print("no such file exists")
except Error