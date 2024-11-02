def get_number_of_squares(n):
    count = 0
    square_sum = 0
    while square_sum < n:
        count += 1
        square_sum += count**2
    return count-1