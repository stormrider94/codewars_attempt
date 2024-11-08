def convert_word(word):
    converted_word = ""
    for i,letter in enumerate(word):
        if i%2 == 0:
            converted_word += letter.upper()
        else:
            converted_word += letter.lower()
    return converted_word
            


def to_weird_case(words):
    final_word = ""
    
    # we need to start all over if there are multiple words 
    if " " in words:
        word_li = words.split(" ")
        for word in word_li:
            final_word += convert_word(word)
            # if it's not the last word, append a space
            if word_li.index(word)!= len(word_li)-1:
                final_word += " "
        print(final_word)
        return final_word
    else:
        final_word = convert_word(words)
        print(final_word)
        return final_word
        
            