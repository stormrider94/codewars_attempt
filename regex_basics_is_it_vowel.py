def is_vowel(s):
    if s == "":
        return False
    if len(s) == 1 and s in "AEIOUaeiou":
        return True
    else:
        return False