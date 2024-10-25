def nothing_special(st):
    if type(st) != str:
        return "Not a string!"
    final_str = ""
    for ch in st:
        if ch.isalpha() or ch in ["\t"," ","\r","\n","\f","\v"] or ch.isdigit():
            final_str += ch
    return final_str