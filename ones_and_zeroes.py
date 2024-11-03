def binary_array_to_number(arr):
    decimal = 0
    for i in range(len(arr)):
        decimal += arr[i] * (2**(len(arr)-i-1))
    return decimal