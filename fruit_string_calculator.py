import re
def calculate(strng):
    dig_1 = int(re.search(r'(\d+)\s*',strng).group())
    expression_and_dig_2 = re.search(r'(loses|gains)\s*(\d+)',strng)
    expression,dig_str_2 = expression_and_dig_2.group().split(' ')
    if expression == 'loses':
        return dig_1 - int(dig_str_2)
    elif expression == 'gains':
        return dig_1 + int(dig_str_2)