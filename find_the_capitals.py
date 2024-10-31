def capitals(word):
    indices = []
    for i,letter in enumerate(word):
        if letter.isupper():
            indices.append(i)
    return indices