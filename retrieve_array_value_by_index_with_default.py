def solution(items, index, default_value):
    try:
        val = items[index]
    except IndexError:
        return default_value
    else:
        return val