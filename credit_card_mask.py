def maskify(cc):
    cc_len = len(cc)
    masked_cc = ""
    for i,digit in enumerate(cc):
        if -1*(cc_len-i) >= -4:
            masked_cc += digit
        else:
            masked_cc += '#'
    return masked_cc