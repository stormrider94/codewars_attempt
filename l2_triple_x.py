def triple_x(s):
    index = s.find('x')
    if index != -1 and s[index + 1 : index + 3] == 'xx':
        return True
    return False