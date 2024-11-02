def amount_of_pages(summary):
    digits_sum = 0
    current_page = 0
    if summary == 0:
        return 0
    while digits_sum < summary : 
        current_page += 1
        digits_sum += len(list(str(current_page)))
    print(current_page)
    return current_page