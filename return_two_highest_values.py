def two_highest(arg1):
    unique_vals = list(set(arg1))
    vals_sorted = sorted(unique_vals, reverse=True)
    return vals_sorted[:2]
    