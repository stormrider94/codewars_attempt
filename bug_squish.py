def debug(s):
    resulting_str = ""
    index = 0
    while index < len(s):
        if (s[index : index + 3] == 'bug') and (s[index : index + 4] != 'bugs'):
            # meaing we skip the word bug
            index += 3
        else:
            resulting_str += s[index]
            index += 1
            
    return resulting_str