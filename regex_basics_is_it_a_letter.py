def is_letter(s):
    if isinstance(s,str) and len(s) == 1:
        if s.isalpha() and ord(s) < 128:
            return True
    return False