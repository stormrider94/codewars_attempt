def find_it(seq):
    return [integer for integer in seq if seq.count(integer)% 2 == 1].pop()