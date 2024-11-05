def better_than_average(class_points, your_points):
    sum = 0
    for point in class_points:
        sum += point
    avg = sum / len(class_points)
    return your_points > avg