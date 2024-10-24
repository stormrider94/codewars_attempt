geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    for bird in [*birds]:
        if bird in geese:
            birds.remove(bird)
    return birds