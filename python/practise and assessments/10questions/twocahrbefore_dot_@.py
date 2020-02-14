import re
aa=input("enter string")
if re.match("[\w]{2,64}@[a-zA-Z]{2,10}\.[a-zA-Z]{2,3}",aa):
    print (aa,"is a valid e-mail address")
else:
    print("its not a valid email adderess")






#ip
# "aajdgkashgdk@lajshdl.com arar@asd.com kashdk@asd.com k@sd.com"
#op
# ['aajdgkashgdk@lajshdl.com', 'arar@asd.com', 'kashdk@asd.com']