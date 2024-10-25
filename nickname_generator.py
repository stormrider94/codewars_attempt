def nickname_generator(name):
    if len(name)<4:
        return 'Error: Name too short'
    elif name[2] not in "aeiouAEIOU":
        return name[:3]
    else:
        return name[:4]