def remove_duplicate_words(s):
    single_words = []
    words = s.split(' ')
    for word in words:
        if word not in single_words:
            single_words.append(word)
    return ' '.join(single_words)