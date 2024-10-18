def vowel_2_index(string):
    return_str = ""
    for i,letter in enumerate(list(string)):
        if letter in "AEIOUaeiou":
            return_str += str(i+1)
        else:
            return_str += letter
    return return_str