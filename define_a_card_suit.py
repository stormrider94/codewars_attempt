def define_suit(card):
    cards_dict = {"C":"clubs","D":"diamonds","H":"hearts","S":"spades"}
    x = list(card)[-1] 
    return cards_dict[x]