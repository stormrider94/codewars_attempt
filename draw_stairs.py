def draw_stairs(n):
    stairs = ""
    for i in range(n-1):
        stairs += f"{' '* i}I\n"
    stairs += f"{' '* (i+1)}I"
    return stairs