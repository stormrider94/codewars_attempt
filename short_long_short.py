def solution(a, b):
    short,long = [a,b] if len(b)>len(a) else [b,a]
    return f"{short}{long}{short}"