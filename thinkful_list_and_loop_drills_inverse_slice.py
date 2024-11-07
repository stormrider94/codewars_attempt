def inverse_slice(items, a, b):
    list1 = items
    list2 = items[a:b]
    list_diff = [item for item in list1 if item not in list2]
    return list_diff