def missing(nums, s):
    new_str = "".join(s.split())
    return_str = ""
    for num in sorted(nums):
        try:
            val = new_str[num]
        except:
            return "No mission today"
        else:
            return_str += val
    return return_str.lower()