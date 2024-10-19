def sum_dig_pow(a, b):
    nums_which_satisfy = []
    for i in range(a,b+1):
        total = 0
        for j,val in enumerate(str(i)):
            total += int(val) ** (j+1)
        if total == i:
            nums_which_satisfy.append(i)
    print(nums_which_satisfy)
    return nums_which_satisfy
            