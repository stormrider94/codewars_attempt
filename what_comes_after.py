def comes_after(st, l):
    strng = ''
    for i in range(len(st)):
        if st[i].lower() == l.lower() and  i != len(st)-1 and st[i+1].isalpha():
            strng += st[i+1]
    return strng
            