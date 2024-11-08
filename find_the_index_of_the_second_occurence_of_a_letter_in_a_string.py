def second_symbol(s, symbol):
    #find all occurences of the letter s in the symbol 
    #push all of them into a list
    # return the 2nd index of that list but if the list is empty, return -1
    print(s)
    indexes_of_occurence = []
    for index,char in enumerate(s):
        if char == symbol:
            indexes_of_occurence.append(index)
    print(indexes_of_occurence)
    return indexes_of_occurence[1] if len(indexes_of_occurence) > 1 else -1