def shifted_diff(first, second):
    # how many times should we shift the first to get the second. let's call it n 
    if first == second:
        return 0
    for i in range(len(first)):
        shifted_word = first[-i:] + first[:len(first)-i]
        if shifted_word == second:
            return i
    # we never got a valid shift 
    return -1