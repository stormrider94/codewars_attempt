def points(games):
    total_points = 0
    for score in games:
        x,y = [int(val) for val in score.split(":")]
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
    return total_points