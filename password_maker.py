def make_password(phrase):
    password = ""
    for word in phrase.split():
        print(word)
        if word[0] in ('i','I'):
            password += '1'
            continue
        elif word[0] in ('o','O'):
            password += '0'
            continue
        elif word[0] in ('s','S'):
            password += '5'
            continue
        password += word[0]
    return password