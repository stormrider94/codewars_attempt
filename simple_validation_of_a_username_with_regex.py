def validate_usr(username):
    for x in username:
        if (not x.islower()) and (not x.isdigit()) and (x != "_"):
            return False
    if len(username) < 4 or len(username) > 16:
        return False
    return True