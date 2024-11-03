def people_with_age_drink(age):
    age_drinks = {"child" : "toddy", "teen" : "coke","young adult": "beer", "adult" : "whisky"}
    if age < 14:
        age_group = "child"
    elif age < 18:
        age_group = "teen"
    elif age < 21:
        age_group = "young adult"
    else:
        age_group = "adult"
    return f"drink {age_drinks[age_group]}"