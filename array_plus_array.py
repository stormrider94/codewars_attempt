def array_plus_array(arr1,arr2):
    bigger_array = [*arr1,*arr2]
    sum = 0
    for val in bigger_array:
        sum += val
    return sum