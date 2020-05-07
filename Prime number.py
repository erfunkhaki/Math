def prime(x):
    cal1 = pow(x, 0.5)
    cal2 = round(cal1, 0)
    if x == 2 or x == 3 or x == 5 or x == 7:
        print("Yes it is a prime number")
    elif x == 1 or x == 4 or x == 6 or x == 8 or x == 9:
        print("No it is not a prime number")
    else:        
        for y in range(2, int(cal2)):
            answer = x % int(y)
            if answer == 0:
                print("No it is not a prime number")
                break
            else:
                continue
        else:
            print("Yes it is a prime number")

