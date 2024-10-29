def all_continents(lst):
    continents = []
    for dev in lst:
        if dev["continent"] not in continents:
            continents.append(dev["continent"])
    return len(continents) == 5