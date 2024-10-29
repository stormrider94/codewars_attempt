def is_same_language(lst):
    languages = []
    for dev in lst:
        if dev['language'] not in languages:
            languages.append(dev['language'])
    return len(languages) == 1