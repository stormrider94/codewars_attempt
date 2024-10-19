def double_check(strng):
    has_double = False
    for i in range(len(strng)-1):
        if strng[i].lower() == strng[i+1].lower():
            has_double = True
    return has_double
        