def count(s):
    final_dic = {}
    # The function code should be here
    if s == "":
        return final_dic
    for char in s:
        occurence = s.count(char)
        final_dic[char] = occurence
    return final_dic
        