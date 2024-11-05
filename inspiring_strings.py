def longest_word(string_of_words):
    words = string_of_words.split()
    max_index = 0
    max = len(words[max_index])
    max_word = words[max_index]
    for i in range(len(words)):
        if len(words[i]) > len(max_word):
            max_word = words[i]
            max_index = i
        elif ((len(words[i]) == len(max_word)) and (i > max_index)):
            max_word = words[i]
            max_index = i
        
    print(string_of_words)
    return max_word
        