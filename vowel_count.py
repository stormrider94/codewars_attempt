def get_count(sentence):
    count = 0
    for letter in sentence:
        if letter in "AEIOUaeiou":
            count += 1
    return count