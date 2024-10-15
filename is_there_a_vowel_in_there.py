def is_vow(inp):
    vowel_ord_dict = {ord(x):x for x in ['a','e','i','o','u']}
    for i,x in enumerate(inp):
        if x in vowel_ord_dict:
            inp[i] = vowel_ord_dict[x]
    return inp