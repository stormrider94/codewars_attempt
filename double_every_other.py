def double_every_other(lst):
    li = []
    for i in range(len(lst)):
        if i%2==1 and i!=0:
            li.append(lst[i] * 2)
            continue
        else:
            li.append(lst[i])
    return li
        