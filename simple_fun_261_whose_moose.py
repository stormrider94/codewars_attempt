def whose_move(last_player, win):
    if last_player == 'black' and win:
        return 'black'
    elif last_player == 'black' and not win:
        return 'white'
    elif last_player == 'white' and win:
        return 'white'
    else:
        return 'black'