def fake_bin(x):
    return_str = ""
    for str_digit in x:
        if int(str_digit) >= 5:
            return_str += '1'
        elif int(str_digit) < 5:
            return_str += '0'
    return return_str