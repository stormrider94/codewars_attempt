def nba_extrap(ppg, mpg):
    if not mpg :
        return 0
    # let's find how many points the player can score in a minute per game
    average_points_per_minute = ppg/mpg
    # points that can be scored in 48 minutes depending on the average points per minute
    return round(average_points_per_minute * 48,1)