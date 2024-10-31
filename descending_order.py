def descending_order(num):
    int_li = [int(val) for val in list(str(num))]
    return int("".join(str(val) for val in list(sorted(int_li,reverse=True))))