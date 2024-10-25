def good_vs_evil(good, evil):
    good_total_power = 0
    evil_total_power = 0
    for count,power in zip([int(val) for val in good.split(" ")],[1,2,3,3,4,10]):
        good_total_power += count * power
        
    for count,power in zip([int(val) for val in evil.split(" ")],[1,2,2,2,3,5,10]):
        evil_total_power += count * power
        
    print("good_total_power", " " ,good_total_power)
    print("evil_total_power", " ", evil_total_power)
    if good_total_power > evil_total_power:
        return "Battle Result: Good triumphs over Evil"
    elif good_total_power == evil_total_power:
        return "Battle Result: No victor on this battle field"
    else:
        return "Battle Result: Evil eradicates all trace of Good"