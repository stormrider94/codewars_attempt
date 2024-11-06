def same_case(a, b):
    is_same_case = (a.isupper() and b.isupper()) or (a.islower() and b.islower())
    if (a.isalpha() == False) or (b.isalpha() == False):
        return -1
    elif is_same_case:
        return 1 
    elif (a.isalpha() and b.isalpha()) and not is_same_case: 
        return 0
    