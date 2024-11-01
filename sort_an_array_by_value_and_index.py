def sort_by_value_and_index(arr):
    return [item[1] for item in sorted(enumerate(arr), key = lambda item: (item[0]+1) * item[1] )]