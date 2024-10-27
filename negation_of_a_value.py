def negation_value(s, val):
    if len(s) % 2 == 1:
        return not bool(val)
    else:
        return bool(val)

