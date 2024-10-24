def find_multiples(integer, limit):
    multiples_li = []
    #start,stop,step
    for i in range(0,limit+1,integer):
        if i == 0 or (i%integer != 0):
            pass
        else:
            multiples_li.append(i)
    return multiples_li