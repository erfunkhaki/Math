def linear_spline(points):

    equations = []

    for x in range(len(points)-1):
        current_point = points[x]
        next_point = points[x+1]
        m = slope(current_point, next_point)
        b = y_intercept(m, current_point[0], current_point[1])
        equation = ""
        string_m = str(m)
        string_x =  'x'
        string_b = str(b)
        if(b < 0):
            sign = ' - '
        else:
            sign = ' + '
        equation = string_m + string_x + sign + string_b
        equations.append(equation)
    print("The linear spline is: " + str(equations))
    

def slope(point1, point2):
    return (point2[1] - point1[1])/(point2[0] - point1[0])

def y_intercept(m, x, y):
    b = y - m*x
    return b


message = "Please input x values in ascending in nested brackets:"
print(message)
#points = [[-1,0],[0,1],[1,3]]
#linear_spline(points)
