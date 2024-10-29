def password(st):
    has_upper = any(char.isupper() for char in st)
    has_lower = any(char.islower() for char in st)
    has_digit = any(char.isdigit() for char in st)
    is_valid_length = len(st) >= 8
    return has_upper and has_lower and has_digit and is_valid_length