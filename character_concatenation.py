def char_concat(word):
    print(word)
    reversed_word = word[::-1]
    actual_word = word
    count = 1
    final_str =""
    #if the length of the string is even, we do the normal method
    if(len(word)%2 == 0):
        print("length is even")
        for x,y in list(zip(actual_word,reversed_word))[:len(word)//2]:
            final_str+=x+y
            final_str+=str(count)

            # we then increment count 
            count+=1
        print(final_str)
    else:
        print("length is odd")
        # we remove the central character from both reversed word and actual word
        central_index = len(word)//2
        # we create a list from the word and just remove that specific index
        actual_word_li = list(word)
        actual_word_li.pop(central_index)
        actual_word = "".join(actual_word_li)
        
        reversed_word = actual_word[::-1]
        for x,y in list(zip(actual_word,reversed_word))[:len(actual_word)//2]:
            final_str+=x+y
            final_str+=str(count)

            # we then increment count 
            count+=1
        print(final_str)
    return final_str