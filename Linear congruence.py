def linear_congruence(a, c, m):
    if c % GCD(m, a) != 0:
        print("No solution")
        return
    x = 0    
    solutions = ""
    while(x < m): 
        if((a*x)%m == c): 
           solutions = solutions  + str(x) + " and "
        x += 1   
    print("Your solutions are "+solutions+ "that's it.")
