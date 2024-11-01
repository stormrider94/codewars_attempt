def max_diff(lst):
    if not lst or len(lst) == 1:
        return 0
    return max(lst) - min(lst)