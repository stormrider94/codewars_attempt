def sum_of_differences(arr):
    arr.sort()
    sum = 0
    starting_index = len(arr)-1
    for _ in range(len(arr)-1):
        sum+=arr[starting_index]-(arr[starting_index-1])
        starting_index -= 1
    return sum