def number_to_pwr(number, p):
    x = 1
    for i in range(p):
        x *= number
    print(str(number) + ' raised to ' +str(p)  + f' {x} ')
    return x