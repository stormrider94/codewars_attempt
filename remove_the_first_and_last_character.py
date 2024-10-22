def array(string):
    val_split = string.split(",")
    if len(val_split)<= 2:
        return None
    modified_val =  [x if (i != 0 and i!= len(val_split)-1) else "" for i,x in enumerate(val_split)]
    return " ".join(modified_val).strip()