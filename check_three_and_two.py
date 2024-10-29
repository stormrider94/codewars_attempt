def check_three_and_two(array):
    contains_threes_condition = False
    contains_twos_condition = False
    dict_count = {}
    for val in array:
        if val not in dict_count:
            dict_count[val] = 1
        else:
            dict_count[val] += 1
    for val in dict_count:
        if dict_count[val] == 3:
            contains_threes_condition = True
        elif dict_count[val] == 2:
            contains_twos_condition = True
    return contains_threes_condition and contains_twos_condition