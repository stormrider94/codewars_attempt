def find_missing_letter(chars):
    val_1 = ord(chars[0])
    for char in chars:
        if val_1 != ord(char):
            return chr(val_1)
        val_1 += 1