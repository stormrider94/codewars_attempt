def get_first_python(users):
    python_devs = list(filter(lambda x: x["language"] == "Python", users))
    if not python_devs:
        return "There will be no Python developers"
    return f"{python_devs[0]['first_name']}, {python_devs[0]['country']}"