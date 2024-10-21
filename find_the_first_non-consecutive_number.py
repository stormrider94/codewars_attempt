def first_non_consecutive(arr):
    for i,val in enumerate(arr):
        if i == 0:
            continue
        if arr[i-1] + 1 != val:
            return val
    return None