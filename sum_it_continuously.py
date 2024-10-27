def add(lst):
    current_sum = 0
    new_li = []
    for num in lst:
        current_sum += num
        new_li.append(current_sum)
    return new_li
        
