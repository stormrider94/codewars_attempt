def get_number_from_string(st):
    num_val = ""
    for val in st:
        if not val.isdigit():
            continue
        num_val += val
    return int(num_val)