def is_age_diverse(lst):
    if len(lst) == 0:
        return False
    age_groups_dict = {
        "teens" : 0,
        "twenties" : 0,
        "thirties": 0,
        "forties": 0,
        "fifties": 0,
        "sixties" : 0,
        "seventies" : 0,
        "eighties" : 0,
        "nineties": 0,
        "centenarian": 0
    }
    for dev in lst:
        if dev['age'] < 20:
            age_groups_dict['teens'] += 1
        elif dev['age'] < 30:
            age_groups_dict['twenties'] += 1
        elif dev['age'] < 40:
            age_groups_dict['thirties'] += 1
        elif dev['age'] < 50:
            age_groups_dict['forties'] += 1
        elif dev['age'] < 60:
            age_groups_dict["fifties"] += 1
        elif dev['age'] < 70:
            age_groups_dict['sixties'] += 1
        elif dev['age'] < 80:
            age_groups_dict['seventies'] += 1 
        elif dev['age'] < 90:
            age_groups_dict['eighties']  += 1
        elif dev['age'] < 100:
            age_groups_dict['nineties'] += 1
        elif dev['age'] >= 100:
            age_groups_dict['centenarian'] += 1
    print(age_groups_dict)
            
    for age_group in age_groups_dict:
        if age_groups_dict[age_group] == 0:
            return False
    print(lst)
    return True