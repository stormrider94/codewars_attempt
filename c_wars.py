def initials(name):
    name_with_initials = ""
    names = name.split()
    last_name = names[-1].title()
    for name in names[:-1]:
        name_with_initials += name[0].upper() + '.'
    name_with_initials += last_name
    return name_with_initials

print(initials('code wars'))  # C.Wars
print(initials('Barack hussein obama')) # B.H.Obama
print(initials('barack hussein Obama')) # B.H.Obama



