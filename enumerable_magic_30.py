def partition(arr, classifier_method):
    satisfies_condition = list(filter(classifier_method,arr))
    remaining_elems = []
    for x in arr:
        if x not in satisfies_condition:
            remaining_elems.append(x)
    return (satisfies_condition,remaining_elems)