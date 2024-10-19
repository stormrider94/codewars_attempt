def num_key_strokes(text):
    total_no_keystrokes = 0
    for key in text:
        if key.isupper() or key in ':"<>?{}|_+~!@#$%^&*()"':
            keystroke = 2
        else:
            keystroke = 1
        total_no_keystrokes += keystroke
    return total_no_keystrokes