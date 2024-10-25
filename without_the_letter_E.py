def find_e(s):
    if s == None:
        return None
    elif len(s) == 0:
        return ''
    e_counter = 0
    for ch in s:
        if ch == 'e' or ch == 'E':
            e_counter += 1
    if e_counter == 0:
        return 'There is no "e".'
    else:
        return str(e_counter)
    