def replace_exclamation(st):
    new_st = ""
    for char in st:
        new_st += char if char not in "aeiouAEIOU" else '!'
    return new_st
        
        