def warn_the_sheep(queue):
    if 'sheep' not in queue:
        return "Pls go away and stop eating my sheep"
    queue.reverse()
    wolf_index,sheep_index = queue.index('wolf'),queue.index('sheep')
    return "Pls go away and stop eating my sheep" if wolf_index < sheep_index else f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!"