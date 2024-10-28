def next_letter(s):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    altered_s = ''
    for char in s:
        if char.lower() in letters:
            if char.isupper():
                altered_s += letters[letters.index(char.lower()) + 1].upper()
            else:
                altered_s += letters[letters.index(char) + 1]
        else:
            altered_s += char
    return altered_s