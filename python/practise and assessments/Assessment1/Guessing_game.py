import random
numbers=[]
for i in range(0,10):
    if i not in numbers:
        numbers.append(random.randrange(0,50))
print(numbers)
number=random.choice(numbers)
print(number)
print("could u find the number??? then enter : ")
for x in range(3):
    guess = int (input ())
    if x<=1:
        if guess==number:
            print("yay! you guessed correctly")
            break
        elif guess<=number+5 and guess>=number-5:
            print("you are close,try again")

        else:
            print("give a wild guess: ")
    else:
        if guess==number:
            print("yay! you guessed correctly: ")
            break
        else:
            print("oops you are outta chances,better luck next time.")

