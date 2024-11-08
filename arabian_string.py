def camelize(str_):
    print(str_)
    final_str = ""
    skip_next_iteration = False
    for i,char in enumerate(str_):
        if skip_next_iteration:
            skip_next_iteration = False
            continue
        if char.isalnum():
            if i == 0:
                final_str+= char.upper()
            else:
                final_str += char.lower()
        else:
            if i != len(str_)-1:
                if str_[i+1].isalnum():
                    # skip the next iteration 
                    skip_next_iteration = True
                    final_str += str_[i+1].upper()
            # what if it is an alpha-numberic character and it also is the last character
            else:
                # don't add it to the final_str
                pass
    #print(str_)
    print(final_str)
    return final_str