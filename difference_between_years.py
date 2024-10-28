import re
def how_many_years (date1,date2):
    year_regex = re.compile(r'(\d)+/')
    year_1 = year_regex.search(date1).group()[:-1]
    year_2 = year_regex.search(date2).group()[:-1]
    return abs(int(year_1) - int(year_2))