def dashatize(n):
    dashatized_str = ''
    n_li = list(str(abs(n)))
    for i,digit in enumerate(n_li):
        if i == 0:
            if len(n_li) == 1:
                dashatized_str += digit
            elif int(digit) % 2 == 1:
                dashatized_str += f'{digit}-'
            else:
                dashatized_str += digit 
        elif i == len(n_li) - 1:
            if int(digit) % 2 == 0:
                dashatized_str += digit
            else:
                if int(n_li[i-1])%2 == 1:
                    dashatized_str += f'{digit}'
                else:
                    dashatized_str += f'-{digit}'                
        else:
            if int(digit) % 2 == 1:
                if int(n_li[i-1])%2 == 1:
                    dashatized_str += f'{digit}-'
                else:
                    dashatized_str += f'-{digit}-'
            else:
                dashatized_str += digit

    return dashatized_str

print(dashatize(274))
print(dashatize(5311))
print(dashatize(86320))
print(dashatize(974302))
print(dashatize(0))
print(dashatize(-1))
print(dashatize(-28369))


