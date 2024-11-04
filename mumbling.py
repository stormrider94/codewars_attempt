def accum(s):
    final_str = ""
    for i in range(len(s)):
        final_str += f"{s[i].upper()}{s[i].lower() * (i)}"
        if i!= len(s)-1:
            final_str += '-'
    return final_str
            