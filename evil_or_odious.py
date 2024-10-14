def evil(n):
    n_binary = bin(n).split('0b')[1]
    return "It's Evil!" if n_binary.count('1')%2==0 else "It's Odious!"