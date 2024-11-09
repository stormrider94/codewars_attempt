def sort_array(source_array):
    odds_from_source=[el for el in source_array if el%2]
    odds_arranged=iter(sorted(odds_from_source))
    arr_with_only_odds_sorted=[next(odds_arranged) if el%2 else el for el in source_array]
    print(arr_with_only_odds_sorted)
    return arr_with_only_odds_sorted

#it seems in order to use the next function, you have to use an iterable