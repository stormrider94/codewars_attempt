def is_opposite(s1,s2):
    if (not s1) or (not s2):
        return False
    s1_alternate = "".join([letter.lower() if letter.isupper() else letter.upper() for letter in list(s1)])
    return s2 == s1_alternate