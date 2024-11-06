def calc_poly(coefficients, x):
    # Initialize an empty string to build the polynomial representation
    poly_str = "For "
    
    # Check if the first coefficient is -1 and handle accordingly
    if coefficients[0] == -1:
        poly_str += "-x^" + str(len(coefficients) - 1)
    elif coefficients[0] == 1:
        poly_str += "x^" + str(len(coefficients) - 1)
    elif coefficients[0] == 0:
        poly_str += ""
    else:
        poly_str += str(coefficients[0]) + "*x^" + str(len(coefficients) - 1)
    
    # Iterate through the remaining coefficients
    for i in range(1, len(coefficients)):
        if coefficients[i] == 0:
            continue  # Skip terms with a coefficient of 0
        # elif the index of the element before this element is the first element and it's index is 0 append "+" instead of the conventional " + "
        elif (coefficients[i] > 0) and (coefficients[i-1] == 0) and (i-1 == 0):
            poly_str += "+"
        elif (coefficients[i] < 0) and (coefficients[i-1] == 0) and (i-1 == 0):
            poly_str += "-"
        elif (coefficients[i] > 0) and (coefficients[0:i] == [0] * i):
            poly_str += "+"
        elif (coefficients[i] < 0) and (coefficients[0:i] == [0] * i):
            poly_str += "-"
        elif coefficients[i]> 0:
            poly_str += " + "         
        elif coefficients[i]< 0:
            poly_str += " - "
        
        # Handle the case where the coefficient is 1
        if abs(coefficients[i]) == 1:
            if len(coefficients)-1-i == 1:
                poly_str += "x"
            elif len(coefficients)-1-i == 0:
                poly_str += str(abs(coefficients[i]))
            else:
                poly_str += "x^" + str(len(coefficients) - 1 - i)
        else:
            if len(coefficients)-1-i == 1:
                poly_str += str(abs(coefficients[i])) + "*x"
            elif len(coefficients)-1-i == 0:
                poly_str += str(abs(coefficients[i]))
            else:
                poly_str += str(abs(coefficients[i])) + "*x^" + str(len(coefficients) - 1 - i)
    
    # Add the final part of the string with the value of x
    poly_str += " with x = " + str(x) + " the value is " + str(sum(c * (x ** (len(coefficients) - 1 - i)) for i, c in enumerate(coefficients)))
    
    return poly_str

# [6, 3, 5, -4], 4 
# "For 6*x^3 + 3*x^2 + 5*x - 4 with x = 4 the value is 448"

# [2, 0, 5, -6, 4, 0], 2
# "For 2*x^5 + 5*x^3 - 6*x^2 + 4*x with x = 2 the value is 88"

# Test failed with pol_list = [6, 3, 5, -4], x = 4: 'For 6*x^3 + 3*x^2 + 5*x^1 - 4*x^0 with x = 4 the value is 448' should equal 'For 6*x^3 + 3*x^2 + 5*x - 4 with x = 4 the value is 448'
# Test failed with pol_list = [2, 0, 5, -6, 4, 0], x = 2: 'For 2*x^5 + 5*x^3 - 6*x^2 + 4*x^1 with x = 2 the value is 88' should equal 'For 2*x^5 + 5*x^3 - 6*x^2 + 4*x with x = 2 the value is 88'