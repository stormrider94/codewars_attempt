def alphabet_position(text):
    position_str = ""
    for letter in text: 
        if letter.isalpha():
            if not letter.islower():
                letter = letter.lower()
            position = ord(letter) - 96
            position_str += f'{position} '
    print(text,position_str.rstrip(' '))
    return position_str.rstrip(' ')