def create_dict(keys, values):
    dic_to_return = {}
    for key,value in zip(keys,values):
        dic_to_return[key] = value
    for char in keys:
        if char not in dic_to_return.keys():
            dic_to_return[char] = None
    print(dic_to_return)
    return dic_to_return