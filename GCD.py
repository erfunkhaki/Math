def educliedan (a,b): 
    if a < b:
        makeb = a
        a = b
        b = makeb
    r = 10 #Just to run in the loop

    while r > 0:
        r = a % b
        newa = b 
        newb = r
        a = newa
        b = newb
        if r == 0:
            print ("GCD is " + str(newa) + ".") #Final answer
            break

