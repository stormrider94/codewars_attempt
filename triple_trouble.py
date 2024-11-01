def triple_trouble(one, two, three):
    finale = ""
    for triplet in zip(one,two,three):
        finale += ''.join(triplet)
    return finale