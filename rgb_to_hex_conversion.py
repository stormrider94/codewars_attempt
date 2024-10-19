def rgb(r, g, b):
    hex_value = ""
    for val in [r,g,b]:
        if val in list(range(0,256)):
            curr_val = hex(val).split("0x")[1].upper()
            if len(curr_val) == 1:
                curr_val = f"0{curr_val}"
            hex_value += curr_val
        else:
            if val > 255:
                hex_value += hex(255).split("0x")[1].upper()
            else:
                hex_value += f"0{(hex(0).split('0x')[1].upper())}"
    print(hex_value)
    return hex_value