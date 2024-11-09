def greet_developers(lst):
    new_dev=[]
    for dev in lst:
        dev["greeting"]=f"Hi {dev['firstName']}, what do you like the most about {dev['language']}?"
        new_dev.append(dev)
    print(new_dev)
    return new_dev