import re
def remove(st):
    return re.sub(r'!+$','',st)