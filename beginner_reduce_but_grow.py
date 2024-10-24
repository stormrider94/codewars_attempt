def grow(arr):
    multiplier = 1
    for val in arr:
        multiplier *= val
    return multiplier