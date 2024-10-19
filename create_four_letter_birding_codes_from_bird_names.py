def bird_code(arr):
    all_code_names = []
    for name in arr:
        code = get_code_name(name)
        all_code_names.append(code)
    return all_code_names
        
def get_code_name(name):
    bird_code = ""
    name = name.replace("-"," ")
    names_li = name.split(" ")
    names_len = len(names_li)
    
    if names_len == 1:
        bird_code += names_li[-1][:4].upper()
    elif names_len == 2:
        for name in names_li:
            bird_code += name[:2].upper()
    elif names_len == 3:
        for name in names_li[:2]:
            bird_code += name[0].upper() 
        bird_code += names_li[-1][:2].upper()
    else:
        for name in names_li:
            bird_code += name[0].upper()
    print(bird_code)
    return bird_code