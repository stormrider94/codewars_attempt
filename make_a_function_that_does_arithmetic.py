def arithmetic(a, b, operator):
    arithmetic_dict = {'add' : lambda a,b : a+b , 'subtract': lambda a,b : a-b , 'multiply' : lambda a,b : a * b, 'divide': lambda a,b : a / b}
    return arithmetic_dict[operator](a,b)
    