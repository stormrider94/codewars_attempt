def dont_give_me_five(start,end):
    final_val = 0
    interval = range(start,end+1)
    for i in interval:
        if '5' in str(i):
            continue
        final_val += list(interval).count(i)
    return final_val