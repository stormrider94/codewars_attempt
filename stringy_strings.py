def stringy(size):
    val = ""
    alternating_dig = False
    for i in range(size):
        val += '0' if alternating_dig else '1'
        alternating_dig = not alternating_dig
    return val
        