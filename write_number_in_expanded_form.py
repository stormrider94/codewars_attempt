def expanded_form(num):
    num_str_li = list(str(num))
    bigger_li = []
    joined_string_int_li = []
    for i,num_str in enumerate(num_str_li):
        bigger_li.append([n if j== 0 else "0" for j,n in enumerate(num_str_li[i:]) ])
    for i in range(len(bigger_li)):
        joined_string = "".join(bigger_li[i])
        converted_to_num = int(joined_string)
        if converted_to_num != 0:
            joined_string_int_li.append(converted_to_num)
    final_li = []
    for i in range(len(joined_string_int_li)):
        final_li.append(str(joined_string_int_li[i]))
    return_str = " + ".join(final_li)
    print(return_str)
    return return_str