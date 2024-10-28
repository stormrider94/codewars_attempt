def gap(num):
    bin_str = bin(num)[2:]
    zero_gaps = bin_str.split('1')
    if len(zero_gaps) < 2:
        return 0
    
    longest_gap = max(len(gap) for gap in zero_gaps[:-1])
    return longest_gap