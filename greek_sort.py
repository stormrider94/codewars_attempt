def greek_comparator(lhs, rhs):
    # the tuple greek_alphabet is defined in the global namespace
    lhs_index = greek_alphabet.index(lhs)
    rhs_index = greek_alphabet.index(rhs)
    return -1 if lhs_index < rhs_index else 0 if lhs_index == rhs_index else 1