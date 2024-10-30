def add_length(str_):
    word_li = str_.split(" ")
    return [f"{x} {len(x)}" for x in word_li]