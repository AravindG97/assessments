input = [1, 5, 6, 3, 10 ,5]
summ = 0
for x in range(len(input)):
    summ += input[x]
    if summ == sum(input)/2:
        print(x)