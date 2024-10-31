def find_short(s):
    strings_sorted = sorted(s.split(),key=len)
    return len(strings_sorted[0])