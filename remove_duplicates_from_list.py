def distinct(seq):
    sequence_to_return = []
    for val in seq:
        if val not in sequence_to_return:
            sequence_to_return.append(val)
            
    return sequence_to_return