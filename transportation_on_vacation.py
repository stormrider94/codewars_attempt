def rental_car_cost(d):
    rental = d*40 
    if d >= 7:
        rental -=50
    elif d >=3 : 
        rental-=20
    return rental 