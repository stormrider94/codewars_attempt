def check_password(s):
    islowerCount = 0
    isUpperCount = 0
    isDigitCount = 0
    specialSymbolCount = 0
    # this solution that I will provide won't involve regex
    if(len(s)<8 or len(s)>20):
        return "not valid"
    for letter in s:
        if(letter.islower()):
            islowerCount += 1
            continue
        if(letter.isupper()):
            isUpperCount += 1
            continue
        if(letter.isdigit()):
            isDigitCount += 1
            continue
        if(letter in "!@#$%^&*?"):
            specialSymbolCount += 1
            continue 
        return "not valid"
    if islowerCount and isUpperCount and isDigitCount and specialSymbolCount:
        return "valid"
    else:
        return "not valid"
