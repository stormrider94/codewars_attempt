def derive(coefficient, exponent): 
    finale = ""
    prefix = coefficient * exponent
    finale+= f"{prefix}x"
    suffix = exponent - 1
    if suffix != 2:
        finale += f"^{suffix}"
    return finale
        