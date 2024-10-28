def sum_of_a_beach(beach):
    total_count = 0
    beach = beach.lower()
    for val in ['sand','water','fish','sun']:
        if val in beach:
            total_count += beach.count(val)
    return total_count