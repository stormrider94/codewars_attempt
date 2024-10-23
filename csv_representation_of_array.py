def to_csv_text(array):
    final_csv = ""
    for y,li in enumerate(array):
        line = ""
        for i,val in enumerate(li):
            if i < len(li)-1:
                line+= str(val) + ','
            else:
                if y == len(array) - 1:
                    line+= str(val)
                else:
                    line+= str(val) + "\n"
        final_csv+=line
    return final_csv
            