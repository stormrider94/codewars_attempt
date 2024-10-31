def broken(inp):
    corrected_str = ""
    for x in inp:
        if x == '1':
            corrected_str += '0'
        elif x == '0':
            corrected_str += '1'
        else:
            corrected_str += x
    return corrected_str
            