def string_clean(s):
    finale = ""
    for letter in s:
        if not letter.isdigit():
            finale+= letter
    return finale