def cannons_ready(gunners):
    for person in gunners:
        if gunners[person] == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'