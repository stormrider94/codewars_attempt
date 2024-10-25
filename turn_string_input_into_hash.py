def str_to_hash(st):
    if not st:
        return {}
    dict = {}
    for key_val in st.split(", "):
        key,val = key_val.split("=")
        dict[key] = int(val)
    return dict
        