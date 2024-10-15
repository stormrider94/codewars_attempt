def capitalize_word (word : str) -> str:
    word_li = list(word)
    word_li[0] = word[0].upper()
    return "".join(word_li)