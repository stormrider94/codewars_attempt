def assemble(arr):
    if not arr:
        return ""
    first_word = arr[0]
    result = ""
    for i in range(len(first_word)):
        char = first_word[i]
        for j in range(1,len(arr)):
            current_word = arr[j]
            # handle inconsistencies in the list
            if j>len(current_word):
                char = '#'
                result += char
                break
            # if they are equal and char is not a '*'
            elif (char == current_word[i]) and (current_word[i] != '*'):
                result += char
                break
            # if they aren't equal and char is not a '*'
            elif (char != current_word[i]) and (char != '*'):
                result += char
                break
            # if they aren't equal and char is a '*'
            elif (char != current_word[i]) and (char == '*'):
                char = current_word[i]
                result += char
                break
            # if they are both '*'
            elif char == current_word[i] == '*':
                continue
                
        # if after the inner for loop, the char is still a '*'
        if char == '*':
            char = '#'
            result += char
            
                
            
            
                
    print(arr, result)
    return result
            