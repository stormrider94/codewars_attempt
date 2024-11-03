def stray(arr):
    temp_dic = {
    }
    for num in arr:
        if num not in temp_dic:
            temp_dic[num] = 1
        else:
            temp_dic[num] += 1
    # find the only which appears only ones 
    for vals in temp_dic.items():
        if vals[1] == 1:
            return vals[0]