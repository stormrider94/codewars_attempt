def next_item(xs, item):
    it = iter(xs)
    for current in it:
        if current == item:
            try:
                return next(it)
            except StopIteration:
                return None
    return None