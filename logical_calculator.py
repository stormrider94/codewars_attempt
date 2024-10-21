bool_dict = {"XOR":lambda x,y:(x or y) and not(x and y), 'AND':lambda x,y: x and y, 'OR': lambda x,y: x or y}

def logical_calc(array, op):
    starting_index = 0
    resulting_operand = array[starting_index]
    for _ in range(len(array)-1):    
        if op in bool_dict:
            resulting_operand = bool_dict[op](resulting_operand,array[starting_index + 1])
            starting_index += 1
    return resulting_operand