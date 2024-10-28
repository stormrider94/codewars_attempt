import re
def is_valid(idn):
    if len(idn) == 0:
        return False
    idn_regex = re.compile(r'^[a-zA-Z_$][a-zA-Z0-9_$]*$')
    return bool(idn_regex.fullmatch(idn))