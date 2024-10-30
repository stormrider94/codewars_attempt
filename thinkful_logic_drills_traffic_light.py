def update_light(current):
    state_change = {"green": "yellow","yellow":"red","red":"green"}
    return state_change[current]