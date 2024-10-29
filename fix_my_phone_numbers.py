import re
def is_it_a_num(s: str) -> str:
    digits = re.sub('\D','',s)
    if len(digits) == 11 and digits.startswith('0'):
        return digits
    else:
        return 'Not a phone number'