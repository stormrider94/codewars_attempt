def procedure(i):
    final_sum = 0
    for num in range(101):
        if num%i == 0:
            if len(list(str(num))) > 1:
                digit_sum = sum([int(x) for x in list(str(num))])
                final_sum += digit_sum
            else:
                final_sum += num
    return final_sum