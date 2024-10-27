def get_num(n):
    holes = {'0': 1, '6': 1, '8': 2, '9': 1,'1': 0, '2': 0, '3': 0, '4': 0,'5': 0, '7': 0}
    return sum(holes[digit] for digit in str(n))