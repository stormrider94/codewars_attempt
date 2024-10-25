def remove_bmw(string):
    final_str = ''
    if type(string) != str:
        return "This program only works for text"
    for ch in string:
        if ch not in "BMWbmw":
            final_str += ch
    return final_str
            