def check_if_string_ends_with_digits(word):
    # reverse the string
    new_str = reversed(word)
    digits_str_li = []
    # for loop to help us get the numbers
    for char in new_str:
        if char.isdigit():
            digits_str_li.append(char)
        else:
            break
    # if we don't get a single digit just return False
    if len(digits_str_li) == 0:
        return False,None
    # reverse the digits_str_li
    digits_str_li.reverse()
    main_digit = "".join(digits_str_li)
    return True,main_digit
            
    

def increment_string(strng):
    final_str = ""
    # check if the string ends with a number
    ends_with_num,digit_val = check_if_string_ends_with_digits(strng)
    if not ends_with_num:
        final_str = strng+"1"
    # if ends_with_num is true then that means that digit_val has a value and is not None
    else:
        # check if a string starts with a zero
        if digit_val.startswith("0"):
            # convert it to an integer
            incremented = int(digit_val) + 1
            incremented = str(incremented).zfill(len(digit_val))
            final_str = strng.replace(digit_val,incremented)
        else:  
            incremented_val = int(digit_val) + 1
            incremented = str(incremented_val)
            final_str = strng.rstrip(digit_val) + incremented
    print(f"{strng} ===> {final_str}")   
    return final_str