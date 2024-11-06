def solve(s:str) -> int:
    num_li = [] 
    num_vals = ""
    for char in s:
        if char in "0123456789":
            num_vals += char
            
            # check if the num_vals is not empty and append it if it isn't empty
        else:
            # meaning we have encountered a letter
            if num_vals != "":
                num_li.append(int(num_vals))
                num_vals = ""
    # after the loop has ended, push the most recent value of num_vals if it isn't empty
    if num_vals != "":
        num_li.append(int(num_vals))
    return max(num_li)