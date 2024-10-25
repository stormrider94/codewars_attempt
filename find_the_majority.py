def majority(arr):
    if len(arr) == 0:
        return None
    frequencies_dic = {}
    for val in arr:
        if val not in frequencies_dic:
            frequencies_dic[val] = 1
        else:
            frequencies_dic[val] += 1
    # check if the values have the same frequencies of occurence
    max_value = max(frequencies_dic.values())
    max_keys = [key for key,val in frequencies_dic.items() if val == max_value]
    if len(max_keys) == 1:
        return max_keys[0]
    else:
        return None