def high_and_low(numbers):
    num_li = [int(x) for x in numbers.split()]
    return f"{max(num_li)} {min(num_li)}"