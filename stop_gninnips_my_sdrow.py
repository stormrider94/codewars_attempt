def spin_words(sentence):
    words = sentence.split()
    new_words  = []
    for word in words: 
        if len(word) < 5:
            new_words.append(word)
            continue
        new_words.append(word[::-1])
    print(" ".join(new_words))
    return " ".join(new_words)