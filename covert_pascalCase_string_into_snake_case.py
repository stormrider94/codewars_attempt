def handle_multiple_indices(word,letter,index):
    if word.count(letter) == 1:
        idx = word.index(letter)
    else:
        for i,char in enumerate(word):
            if i == index and char == letter:
                idx = i
    return idx

def to_underscore(string):
    print(string)
    final_string = ""
    # cases where string is actually an integer
    if type(string) == int:
        final_string += str(string)
        print(final_string)
        return final_string
    for i,letter in enumerate(string):
        if type(letter) == int:
            final_string += str(letter)
        # meaning the letter is a string
        else:
            if letter.isupper():
                idx = handle_multiple_indices(string,letter,i)
                if idx != 0:
                    final_string +="_"
                    final_string +=letter.lower()
                else:
                    final_string += letter.lower()
            else:
                final_string += letter
                
    print(final_string)
    return final_string
            