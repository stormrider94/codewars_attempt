def next_happy_year(year):
    print(year)
    current_year = year + 1
    # let's first check if the year is distinct and then return it
    count_1 = 0
    for letter in str(current_year):
        if str(current_year).count(letter) == 1:
            count_1 += 1
    if count_1 == len(str(current_year)):
        return current_year
    while True:
        current_year_str = str(current_year)
        count = 0
        for letter in str(current_year):
            if str(current_year).count(letter) == 1:
                count += 1
        if count == len(current_year_str):
            print(current_year)
            return current_year
        
        current_year += 1