def is_language_diverse(lst): 
    javascript_devs=list(filter(lambda dev:dev['language']=="JavaScript" , lst))
    python_devs=list(filter(lambda dev:dev['language']=="Python" , lst))
    ruby_devs=list(filter(lambda dev:dev['language']=="Ruby" , lst))
    if len(python_devs)>2*len(ruby_devs) or len(python_devs)>2*len(javascript_devs):
        return False
    elif len(javascript_devs)>2*len(python_devs) or len(javascript_devs)>2*len(ruby_devs):
        return False
    elif len(ruby_devs)>2*len(javascript_devs) or len(ruby_devs)>2*len(python_devs):
        return False
    else:
        return True