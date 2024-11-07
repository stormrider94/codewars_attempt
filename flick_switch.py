def flick_switch(lst):
    new_li = []
    switch = True
    for element in lst:
        if element == "flick":
            switch = not switch
        new_li.append(switch)
    print(new_li)
    return new_li