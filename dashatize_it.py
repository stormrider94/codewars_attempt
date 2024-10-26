# old source code
def dashatize(n):
    new_str = ''
    n_li = list(str(n))
    # if it's an odd number but it's not the first or the last
    for i,digit in enumerate(n_li):
        digit = int(digit)
        if digit%2 != 0 and (i != 0  and i != len(n_li) - 1):
            new_str += '-'
            new_str += str(digit)
            if int(n_li[i+1])%2 == 0:
                new_str += '-'
            elif int(n_li[i+1])%2 == 1 and (i == len(n_li)):
                new_str += '-'
            continue
        new_str += str(digit)
    return new_str
        
                