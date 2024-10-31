def sequence_sum(begin_number, end_number, step):
    sum = 0
    if begin_number > end_number:
        return 0
    if step <= end_number:
        # don't add end_number to the steps
        end_number += 1
    for x in list(range(begin_number,end_number,step)):
        sum += x
    return sum
    