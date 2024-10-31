def some_but_not_all(sequence, predicate):
    return any(map(predicate, sequence)) and not all(map(predicate, sequence))