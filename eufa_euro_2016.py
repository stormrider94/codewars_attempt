def uefa_euro_2016(teams, scores):
    score_a,score_b = scores
    team_a,team_b = teams 
    message = f"At match {team_a} - {team_b}, "
    if score_a > score_b:
        message += f"{team_a} won!"
    elif score_a < score_b:
        message += f"{team_b} won!"
    else:
        message += "teams played draw."
    return message