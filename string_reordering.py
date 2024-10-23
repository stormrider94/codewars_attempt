def sentence(lst):
    sorted_li = sorted(lst,key=lambda d:int(list(d.keys())[0]))
    output = ""
    for dict in sorted_li:
        print(list(dict.values())[0])
        output += list(dict.values())[0] + " "
    output = output.rstrip()
    return output