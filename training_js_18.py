def split_and_merge(string_, separator):
    new_val = ' '.join([separator.join(list(val)) for val in string_.split()])
    return new_val