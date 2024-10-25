def short_form(s):
    final_str = ""
    for i,ch in enumerate(s):
        if ch in "AEIOUaeiou":
            if i==0 or i == len(s)-1:
                final_str += ch
        else:
            final_str += ch
    print(s,final_str)
    return final_str