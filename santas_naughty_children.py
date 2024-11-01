def find_children(santas_list, children):
    return sorted(set([child for child in children if child in santas_list]))