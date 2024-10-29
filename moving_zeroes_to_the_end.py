def move_zeros(lst):
    zero_count = 0
    final_li = []
    for val in lst:
        if val != 0:
            final_li.append(val)
        else:
            zero_count += 1
    final_li.extend(zero_count * [0])
    return final_li