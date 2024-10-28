def encrypt_this(text):
    if not text:
        return ''
    encrypted_words = []
    words = text.split(' ')
    for word in words:
        encrypted_word = ''
        if len(word) == 1:
            encrypted_word += str(ord(word[0]))
        elif len(word) == 2:
            encrypted_word += str(ord(word[0])) + word[1]
        else:
            encrypted_word = str(ord(word[0])) + word[-1] + word[2:-1] + word[1]
        encrypted_words.append(encrypted_word)
        
    return ' '.join(encrypted_words)