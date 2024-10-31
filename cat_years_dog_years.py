def human_years_cat_years_dog_years(human_years):
    cat_years,dog_years = 0,0
    if human_years == 1:
        cat_years += 15
        dog_years += 15
        return [human_years,cat_years,dog_years]
    elif human_years == 2:
        cat_years += 15 + 9
        dog_years += 15 + 9
        return [human_years,cat_years,dog_years]
    remaining_years = human_years - 2
    cat_years += 15 + 9 
    cat_years += remaining_years * 4
    dog_years += 15 + 9
    dog_years += remaining_years * 5
    return [human_years,cat_years,dog_years]