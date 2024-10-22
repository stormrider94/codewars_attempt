def alias_gen(f_name, l_name):
    if f_name[0].isalpha() and l_name[0].isalpha():
        alias = FIRST_NAME[f_name[0].upper()] + " " + SURNAME[l_name[0].upper()]
    else:
        return 'Your name must start with a letter from A - Z.'
    return alias