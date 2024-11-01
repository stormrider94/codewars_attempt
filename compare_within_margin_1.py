def close_compare(a, b, margin=0):
    # a is close to b
    if margin >= abs(a-b):
        return 0
    elif a < b:
        return -1
    elif a > b:
        return 1