def convert (a,b):
    if a < b: 
        a = q
    q = 10
    r = 10
    answer = ""
    while q > 0:
        r = a%b
        q = a//b
        a = q
        answer = str(r) + answer 
        if q == 0:
            print (str(answer))
            break



