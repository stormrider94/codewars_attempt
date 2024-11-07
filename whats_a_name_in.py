def name_in_str(str, name):
    str_1 = str.lower()
    str_2 = name.lower()
    index = 0
    
    print(str_1)
    print(str_2)
    for char in str_1:
        if char == str_2[index]:
            index += 1
        if index == len(str_2):
            return True 
    return False