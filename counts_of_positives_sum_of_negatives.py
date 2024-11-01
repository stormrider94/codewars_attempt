def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count_positives = 0
    sum_negatives = 0
    for val in arr:
        if val > 0:
            count_positives += 1
        elif val < 0:
            sum_negatives += val 
    return [count_positives,sum_negatives]