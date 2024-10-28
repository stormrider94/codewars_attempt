def encode(st):
    encoded_str = ''
    for char in st:
        if char in 'aeiou':
            encoded_str += str('aeiou'.index(char) + 1)
        else:
            encoded_str += char
    return encoded_str
    
def decode(st):
    decoded_str = ''
    for char in st:
        if char in '12345':
            decoded_str += 'aeiou'[int(char)-1]
        else:
            decoded_str += char
    return decoded_str