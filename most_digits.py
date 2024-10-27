def find_longest(arr):
    highest_num_of_digits = 0 
    winner = 0
    for num in arr:
        if len(str(num)) > highest_num_of_digits:
            highest_num_of_digits = len(str(num))
            winner = num
    return winner