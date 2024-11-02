def is_pangram(s):
    counter = 0
    all_alphabets = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    for letter in s:
        if letter in all_alphabets:
            all_alphabets = all_alphabets.replace(letter,"")
    return not all_alphabets