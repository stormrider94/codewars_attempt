def count_languages(lst):
    count_lang_dict = {}
    for dev in lst:
        if dev['language'] not in count_lang_dict:
            count_lang_dict[dev['language']] = 1
        else:
            count_lang_dict[dev['language']] += 1
    return count_lang_dict