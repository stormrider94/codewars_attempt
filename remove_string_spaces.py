def no_space(x):
    letters_only_li = [letter if letter != " " else "" for letter in x]
    return "".join(letters_only_li)