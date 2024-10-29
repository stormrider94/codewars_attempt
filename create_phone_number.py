def create_phone_number(n):
    phone_num_str = ""
    phone_num_str += "("
    for x in n[:3]:
        phone_num_str += str(x)
    phone_num_str += ")"
    phone_num_str += " "
    for y in n[3:6]:
        phone_num_str += str(y)
    phone_num_str += "-"
    for z in n[6:]:
        phone_num_str += str(z)
    return phone_num_str