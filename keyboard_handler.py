def handler(key, is_caps=False, is_shift=False):
    
    if (type(key) != str) or (key == ''):
        return 'KeyError'
    
    # lemme define a variable that has the punctuations inside of it 
    num_str_shift_pairings = {
        "1" : "!",
        "2" : "@",
        "3" : "#",
        "4" : "$",
        "5" : "%",
        "6" : "^",
        "7" : "&",
        "8" : "*",
        "9" : "(",
        "0" : ")",
        "-" : "_",
        "=" : "+",
        "`" : "~",
        "[" : "{",
        "]" : "}",
        "\\" : '|',
        ";" : ":",
        "\'" : '\"',
        "," : "<",
        "." : ">",
        "/" : "?"
    }
    if key.isupper():
        return 'KeyError'
    elif (key.isalpha() or key.isdigit()) and (len(key) != 1):
        return 'KeyError'
        
    #else block
    if key.isdigit() and is_shift:
        return num_str_shift_pairings[key]
    elif key.isdigit():
        return key
    elif (not key.isdigit()) and (not key.isalpha()) and is_shift:
        return num_str_shift_pairings[key]
        
    elif key.isdigit() and (not is_shift):
        return key
    else:
        if is_caps and is_shift:
            return key
        elif is_caps or is_shift:
            return key.upper()
        else:
            return key