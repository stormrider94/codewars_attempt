import math
tip_amount_dict = {"terrible": 0,"poor":0.05,"good":0.10,"great":0.15,"excellent":0.20}
def calculate_tip(amount, rating):
    if rating.lower() in tip_amount_dict:
        return math.ceil(amount * tip_amount_dict[rating.lower()])
    return "Rating not recognised"