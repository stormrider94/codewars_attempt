from itertools import permutations

def min_permutation(n):
    if n == 0:
        return 0
    num_str_li = list(str(n))
    li_to_permute = num_str_li
    append_infront = ""
    if n < 0:
        li_to_permute = num_str_li[1:]
        append_infront = "-"
    num_permutations = list(permutations(li_to_permute))
    permuted = []
    for li in num_permutations:
        current_perm_str = "".join(list(li))
        if not current_perm_str.startswith('0'):
            permuted.append(current_perm_str)
    chosen_value = min(permuted,key= lambda x: abs(int((x))))
    finale_str = append_infront + chosen_value
    return int(finale_str)