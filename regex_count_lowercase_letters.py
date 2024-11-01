def lowercase_count(strng):
    count = 0
    for letter in strng:
        if letter.islower():
            count += 1
    return count