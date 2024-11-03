def invert(lst):
    new_lst = []
    if not lst:
        return []
    for num in lst:
        if num < 0:
            new_lst.append(-num)
        elif num > 0:
            new_lst.append(-num)
        else:
            new_lst.append(num)
    return new_lst