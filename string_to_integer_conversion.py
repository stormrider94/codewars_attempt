def my_parse_int(strn):
    strn = strn.strip(" ").strip('\t').strip('\n')
    if strn.isdigit():
        return int(strn)
    else:
        return 'NaN'