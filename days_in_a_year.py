def year_days(year):
    days = {"is_leap_year" : 366 , "is_not_leap_year" : 365}
    is_leap_year = False
    if year % 4 == 0:
        if year % 100 != 0:
            is_leap_year = True
        elif year % 400 == 0:
            is_leap_year  = True
    days_in_year = days["is_leap_year"] if is_leap_year else days["is_not_leap_year"]
    return f"{year} has {days_in_year} days"