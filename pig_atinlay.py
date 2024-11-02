def pig_latin(word):
    new_word=""
    if len(word) > 3:
        new_word += word[1:]
        new_word += word[0]
        new_word += "ay"
    else:
        new_word = word
    return new_word