def sum_array(arr):
    if not arr or len(arr)==1:
        return 0
    indices_min_max = [arr.index(min(arr)),arr.index(max(arr))]
    sum = 0
    for i in range(len(arr)):
        if i in indices_min_max:
            continue
        sum+= arr[i]
    return sum