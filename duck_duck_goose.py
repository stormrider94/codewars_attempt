def duck_duck_goose(players, goose):
    index = goose%len(players) - 1 
    return players[index].name