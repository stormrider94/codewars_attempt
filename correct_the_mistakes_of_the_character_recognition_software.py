def correct(s):
    corrected_word = ""
    for letter in s:
        if letter == "5":
            corrected_word += "S"
        elif letter == "0":
            corrected_word += "O"
        elif letter == "1":
            corrected_word += "I"
        else:
            corrected_word += letter 
    return corrected_word