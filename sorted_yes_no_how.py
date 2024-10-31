def is_sorted_and_how(arr):
    arr_sorted_asc = sorted(arr)
    arr_sorted_desc = sorted(arr,reverse=True)
    if arr == arr_sorted_asc:
        return "yes, ascending"
    elif arr == arr_sorted_desc:
        return "yes, descending"
    else:
        return "no"