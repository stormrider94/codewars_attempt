def duplicate_encode(word):
    word = word.lower()
    return_str = ""
    ch_count_dict = {ch : word.count(ch) for ch in word}
    for ch in word:
        if ch_count_dict.get(ch) == 1:
            return_str += "("
        else:
            return_str += ")"
            
    print(return_str)
    return return_str