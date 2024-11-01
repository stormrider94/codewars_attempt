def calculator(x,y,op):
    operator_dict = {'*': lambda x,y: x*y ,'-': lambda x,y: x-y, '/': lambda x,y: x/y ,'+': lambda x,y : x+y}
    if not str(x).isdigit() or not str(y).isdigit() or op not in operator_dict:
        return "unknown value"
    return operator_dict[op](x,y)