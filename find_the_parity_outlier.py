def find_outlier(integers):
    odd_vals = list(filter(lambda x: x % 2,integers))
    even_vals = list(filter(lambda x : not (x % 2),integers))
    if len(odd_vals) == 1:
        return odd_vals.pop()
    else:
        return even_vals.pop()