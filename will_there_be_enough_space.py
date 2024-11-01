def enough(cap, on, wait):
    people_who_can_enter = cap - on 
    return 0 if people_who_can_enter >= wait else wait-people_who_can_enter