import re
def happy_g(st):
    return not re.search(r'(?<!g)g(?!g)',st)