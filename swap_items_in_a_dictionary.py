from collections import defaultdict
def switch_dict(dic):
    keys_by_values = defaultdict(list)
    # iteratve over the dictionary 
    for key,val in dic.items():
        keys_by_values[val].append(key)
    print(dic,keys_by_values)
    return keys_by_values