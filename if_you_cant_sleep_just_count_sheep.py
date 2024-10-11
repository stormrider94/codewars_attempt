def count_sheep(n):
    if not n:
        return ""
    murmur = ""
    for i in range(1,n+1):
        murmur += f"{i} sheep..."
    return murmur