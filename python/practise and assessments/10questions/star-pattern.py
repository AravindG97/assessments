def triangle(n) :
    for i in range (0, n) :
        for x in range (0, n) :
            print (end=" ")
        for y in range (0, i + 1) :
            print ("* ", end="")
        print ("\r")
        n = n - 1

n = 5
triangle (n)
