def heggeleggleggo(word):
    return_str = ""
    for letter in word:
        if letter ==" ":
            return_str += " "
        elif letter not in "AEIOUaeiou":
            return_str += f"{letter}egg"
        else:
            return_str += letter
    print(word,return_str)
    return return_str