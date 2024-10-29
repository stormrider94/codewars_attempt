def get_average(lst):
    total_ages = 0
    for dev in lst:
        total_ages += dev['age']
    mean_age = round(total_ages / len(lst))
    return mean_age