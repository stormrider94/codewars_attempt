import math
def what_century(year):
    century_str = ""
    prefix = ""
    century_no = math.ceil(int(year)/100)
    if str(century_no)[-1] == "1" and str(century_no) != "11":
        prefix = "st"
    elif str(century_no)[-1] == "2" and str(century_no) != "12":
        prefix = "nd"
    elif str(century_no)[-1] == "3" and str(century_no)!= "13":
        prefix = "rd"
    else:
        prefix = "th"
    century_str += f"{century_no}{prefix}"
    return century_str