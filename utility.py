def does_army_win(army, opponent):
    if army == opponent:
        return False
    elif army == 'S':
        if opponent == 'A':
            return False
        else:
            return True
    elif army == 'A':
        if opponent == 'K':
            return False
        else:
            return True
    elif army == 'K':
        if opponent == 'S':
            return False
        else:
            return True
    elif army == 'T':
        return False