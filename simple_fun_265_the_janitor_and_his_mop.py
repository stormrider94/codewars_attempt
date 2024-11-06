def the_janitor(word):
    alphabets_dictionary = {}
    for i in range(97,97+26):
        alphabets_dictionary[chr(i)] = 0
        
    # loop through the word string
    for elem in set(word):
        if word.count(elem) == 0:
            pass
        elif word.count(elem) == 1:
            alphabets_dictionary[elem] += 1
        else:
            difference_val = word.rindex(elem) - word.index(elem) + 1
            alphabets_dictionary[elem] += difference_val
    print(alphabets_dictionary)
    return list(alphabets_dictionary.values())