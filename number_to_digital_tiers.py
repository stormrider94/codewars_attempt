def create_array_of_tiers(n):
    final_arr = []
    cut_off_digit =""
    for dig in str(n):
        cut_off_digit += dig
        final_arr.append(cut_off_digit)
    return final_arr