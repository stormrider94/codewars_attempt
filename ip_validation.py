def is_valid_IP(ip: str) -> bool:
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or (part[0] == '0' and len(part) > 1):
            return False
        if not 0 <= int(part) <= 255:
            return False
    
    return True