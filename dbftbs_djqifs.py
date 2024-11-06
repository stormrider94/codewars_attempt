def encryptor(key, message):
    

    # create a list to store all the alphabets in lowercase 
    # if it's not a number just append. 
    # if the key is greater than 25 we use the formula (key % 25 -1)
    # if the key is less than -25 we use the formula
    alphabets_str = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    encrypted_str = ""
    if abs(key) >= 26:
        if key > 0:
            key %= 26
        else:
            key = key % 26
    for char in message:
        if not char.isalpha():
            encrypted_str += char
            continue
        char_lowcase = char.lower()
        idx = alphabets_str.index(char_lowcase)
        actual_index = idx + key
        encrypted_char = alphabets_str[actual_index] if char.islower() else alphabets_str[actual_index].upper()
        encrypted_str += encrypted_char
    print(encrypted_str)
    return encrypted_str