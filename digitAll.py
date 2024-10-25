def digit_all (x):
    final_str = ''
    if type(x) != str:
        return "Invalid input !"
    elif x == '':
        return ''
    else:
        for ch in x:
            if ch.isdigit():
                final_str += ch
    return final_str