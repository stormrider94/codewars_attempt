import re

def alphanumeric(password):
    valid_regex = re.compile(r'^[a-zA-Z\d]+$')
    return bool(valid_regex.search(password))