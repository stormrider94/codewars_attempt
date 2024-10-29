def duplicate_count(text):
    alph_num_count = {}
    for x in text.lower():
        if x not in alph_num_count:
            alph_num_count[x] = 1
        else:
            alph_num_count[x] += 1
    return len(list(filter(lambda y: y[1] > 1,alph_num_count.items())))