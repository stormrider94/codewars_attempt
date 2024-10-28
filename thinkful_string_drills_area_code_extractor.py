import re
def area_code(text):
    area_code = re.compile(r'\(\d{3}\)')
    mo = area_code.search(text)
    return mo.group().lstrip('(').rstrip(')')
    