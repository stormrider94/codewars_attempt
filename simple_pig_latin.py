def pig_it(text):
    altered_words = []
    if not text:
        return ''
    for word in text.split(' '):
        altered_word = ''
        if len(word) == 1:
            altered_word += word[0] + 'ay' if  word[0].isalpha() else word[0]
        elif len(word) == 2:
            altered_word += word[1] + word[0] + 'ay'
        else:
            altered_word += word[1:] + word[0] + 'ay'
        altered_words.append(altered_word)
    return ' '.join(altered_words)
