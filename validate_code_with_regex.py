def validate_code(code):
    code = str(code)
    return (code.startswith('1') or code.startswith('2') or code.startswith('3'))