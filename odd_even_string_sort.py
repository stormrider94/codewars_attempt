def sort_my_string(s):
    even_group = ""
    odd_group = ""
    for i,letter in enumerate(s):
        if not i%2:
            even_group += letter 
        else:
            odd_group += letter
    return even_group + " " + odd_group