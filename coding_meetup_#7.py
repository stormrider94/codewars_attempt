def find_senior(lst):
#     print(lst)
    old_devs=[]
    oldest_dev=max(lst,key=lambda dev: dev['age'])
    print(oldest_dev)
    for dev in lst:
        if dev['age']==oldest_dev['age']:
            old_devs.append(dev)
    print(old_devs)
    return old_devs