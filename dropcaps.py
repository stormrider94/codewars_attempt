def drop_cap(words):
    words_capitalized = []
    for word in words.split(' '):
        if len(word) > 2:
            words_capitalized.append(word.capitalize())
        else:
            words_capitalized.append(word)
    return ' '.join(words_capitalized)