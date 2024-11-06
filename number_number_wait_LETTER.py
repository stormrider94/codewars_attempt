# when you don't pass a parameter to the split function, it uses 
# it uses whtespace to split the characters 
test_str = "24z6 1x23 y369 89a 900b"
test_str_1 = "24z6 1z23 y369 89z 900b"
def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2
    
operation_order = [add,subtract,multiply,divide]
def do_math(s):
    s_li = s.split()
    letter_num_li = []
    for elem in s_li:
        current_li = []
        elem_num = ""
        for char in elem:
            if not char.isalpha():
                elem_num += char
            else:
                current_li.append(char)
                
        current_li.append(elem_num)
        letter_num_li.append(current_li)
    letter_num_li = sorted(letter_num_li,key = lambda x : x[0])
    print(letter_num_li)
    
    ints_gotten = [int(li[1]) for li in letter_num_li]
    print(ints_gotten)
    
    # let's handle the calculation 
    idx = 0
    result = ints_gotten[0]  # Initialize result with the first number
    for i in range(1, len(ints_gotten)):
        result = operation_order[idx % 4](result, ints_gotten[i])
        idx += 1
        
    print(round(result))
    result = round(result)
    return result
        
        
do_math(test_str)
do_math(test_str_1)
    