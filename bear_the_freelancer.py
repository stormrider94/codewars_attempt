def bear_dollars(jobs):
    total = 0
    for hours,proximity in jobs:
        proximity = proximity.lower()
        if proximity == 'close friend':
            total += hours * 25
        elif proximity == 'friend':
            total += hours * 50
        elif proximity == 'acquaintance':
            total += hours * 100
        else:
            total += hours * 125
    return total