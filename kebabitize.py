import re
def kebabize(st):
    st = re.sub('\d','',st)
    kebab_string = re.sub(r'([A-Z])',r'-\1',st).lower()
    return kebab_string.lstrip('-')