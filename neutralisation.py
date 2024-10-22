def neutralise(s1, s2):
    neutralised = ""
    for sign_a,sign_b in zip(s1,s2):
        if ((sign_a == '+') and (sign_b == "-")) or ((sign_a == "-") and (sign_b == '+')):
            neutralised += '0'
        if sign_a == sign_b:
            neutralised += sign_a
    return neutralised 