def unique_in_order(sequence):
    unique_sequence = []
    for i,val in enumerate(sequence):
        if i == len(sequence) - 1:
            unique_sequence.append(val)
            break
        elif val == sequence[i + 1]:
            continue
        else:
            unique_sequence.append(val)
    return unique_sequence