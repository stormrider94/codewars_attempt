def reverse_vowels(s):
    indices = []
    vowels_found = []
    new_string = ""
    for i,letter in enumerate(s):
        if letter in "AEIOUaeiou":
            indices.append(i)
            vowels_found.append(letter)
            
    # reverse the list of vowels
    vowels_found.reverse()
    for letter in s:
        if letter not in vowels_found:
            new_string += letter
        else:
            new_string += "-"
    # convert the new_string into a list
    new_string_li = list(new_string)
            
    # lemme pair the reversed list of vowels and the indices and put them in a dictionary
    indice_val_paired = list(zip(vowels_found,indices))
    for pair in indice_val_paired:
        vowel = pair[0]
        index = pair[1]
        new_string_li[index] = vowel
        print(index,vowel)
        
    return "".join(new_string_li)