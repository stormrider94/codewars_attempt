def remove_every_other(my_list):
    new_list = [x for i,x in enumerate(my_list) if i%2==0]
    return new_list
