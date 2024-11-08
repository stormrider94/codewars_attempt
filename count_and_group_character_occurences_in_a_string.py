def get_char_count(s):
    final_dic = {}
    occurences = []
    # first let's convert the string to lowercase 
    s= s.lower()
    
    # let's get all the occurrences of all the characters and push them into a list
    for char in s:
        if not char.isalnum():
            continue
        occurences.append(s.count(char))
    occurences = list(set(occurences))
    
    # I have to sort this occurences list
    occurences = sorted(occurences,reverse = True)
    
    for num in occurences:
        final_dic[num] = []
    for char in list(set(s)):
        if (s.count(char) in occurences) and (char.isalnum()) :
            final_dic[s.count(char)].append(char)
        else:
            # how the hell is there even an else loop :)
            pass
        # lemme sort this list as well
    for key in final_dic:
        # permanently sort the positions of the lists within the dictionary
        final_dic[key].sort()
    print(final_dic)
    return final_dic