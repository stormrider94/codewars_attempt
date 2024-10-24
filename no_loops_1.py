def small_enough(a, limit):
    return len(list(filter(lambda x: x <= limit,a))) == len(a)