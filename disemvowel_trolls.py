def disemvowel(string_):
    final_str = ""
    for letter in string_:
        if letter not in "AEIOUaeiou":
            final_str += letter
    return final_str