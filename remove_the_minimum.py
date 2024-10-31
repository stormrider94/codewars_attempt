def remove_smallest(numbers):
    if not numbers:
        return []
    prices = numbers[:]
    lowest_priced = min(numbers)
    prices.remove(lowest_priced)
    return prices