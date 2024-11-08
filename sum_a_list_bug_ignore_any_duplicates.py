import functools
def sum_no_duplicates(l):
    all_elem_count = {}
    no_duplicate_list = []
    print(l)
    for elem in l:
        if elem not in all_elem_count:
            all_elem_count[elem] = 1
        else:
            all_elem_count[elem] += 1
    print(no_duplicate_list)
    for key in all_elem_count:
        if all_elem_count[key] > 1 : 
            continue
        else:
            no_duplicate_list.append(key)
    return functools.reduce(lambda x,y: x + y,no_duplicate_list) if len(no_duplicate_list) != 0 else 0

    
    
    
    
    
    
# we need to remove duplicate items 
# loop through the list and if element already exits, skip the iteratioin