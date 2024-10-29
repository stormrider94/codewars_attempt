def tail_swap(strings):
    list_ab = []
    list_a = []
    list_b = []
    for s in strings:
        list_a.append(s.split(':')[0])
        list_b.insert(0,s.split(':')[1])
    for a,b in list(zip(list_a,list_b)):
        list_ab.append(a + ':' + b)
    return list_ab