def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    new_phrase = phrase[:size]
    if len(new_phrase) > 3:
        new_phrase = new_phrase[:-3]
    new_phrase += "..."
    return new_phrase