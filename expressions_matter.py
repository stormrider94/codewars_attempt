def expression_matter(a, b, c):
    max = 0 
    if a * (b + c) > max:
        max = a * (b + c)
    if a * b * c > max:
        max = a * b * c
    if a + b * c > max:
        max = a + b * c
    if (a + b) * c > max:
        max = (a + b) * c
    if a + b + c > max:
        max = a + b + c
    return max