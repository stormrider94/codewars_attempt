def is_leap_year(year):
    if year % 4 == 0 :
        # it's a leap year but then we have to check if it is divisible by 400
        if year % 100 == 0 and (year % 400 == 0):
            return  True 
        elif year % 100 == 0 and (year % 400 != 0):
            return False
        return True
    return False