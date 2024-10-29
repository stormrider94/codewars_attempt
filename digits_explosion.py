def explode(s):
    final_str = ''
    for val in s:
        final_str+= val * int(val)
    return final_str