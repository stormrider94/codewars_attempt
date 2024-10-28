import re
def rad_ladies(name):
    return re.sub(r'[^a-zA-Z\s!]','',name).upper()