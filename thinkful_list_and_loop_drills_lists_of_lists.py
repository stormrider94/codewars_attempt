def process_data(data):
    difference_li = [li[0]-li[1] for li in data]
    product = 1
    for num in difference_li:
        product *= num
    return product
    