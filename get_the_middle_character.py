def get_middle(s):
    if len(s) % 2 == 0:
        return f"{s[(len(s)//2)-1] + s[len(s)//2]}"
    return s[len(s)//2]