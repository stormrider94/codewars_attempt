def best_friend(txt, a, b):
    print(txt)
    for i in range(len(txt)):
        if i == len(txt)-1 and (txt[i] == a):
            return False
            
        if (txt[i] == a) and (txt[i+1] != b):
            return False
    return True