def sentencify(words):
    sentence = ' '.join(words)
    sentence = sentence[0].upper() + sentence[1:]
    return sentence + '.'