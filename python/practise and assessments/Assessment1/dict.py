a={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"plus":"+","minus":"-","divide":"%","product":"*"}

b=input("enter the string: ")
c=b.split(" ")
d=""
for x in c:
  for y in a:
    if x==y:
      d=d+str(a.get(y))
for x,y in a.items():
  if eval(d)==y:
    print(x)
