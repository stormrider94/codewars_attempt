def to_alternating_case(string):
    return_str = ''
    if string == '':
        return ''
    for letter in string:
        if letter.isalpha():
            if letter.isupper():
                return_str+=letter.lower()
            else:
                return_str+=letter.upper()
        else:
            return_str += letter
    print(f"{string} ==> {return_str}")
    return return_str