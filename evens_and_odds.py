def evens_and_odds(n):
    if n==0:
        return '0'
    elif n%2==0:
        return str(bin(n)).lstrip('0b')
    else:
        return str(hex(n)).lower().lstrip('0x')