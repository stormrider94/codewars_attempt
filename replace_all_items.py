def replace_all(obj, find, replace):
    if isinstance(obj,list):
        return [ replace if val == find else val for val in obj]
    elif isinstance(obj,str):
        new_str = ''
        for val in obj:
            if val == find:
                new_str += replace
            else:
                new_str+= val
        return new_str