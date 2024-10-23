def remove(s):
    if not s:
        return ""
    if s[-1] == "!":
        return s[:-1]
    return s