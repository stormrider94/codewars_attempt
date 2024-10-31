def search_names(logins):
    return list(filter(lambda x: x[0].endswith('_'),logins))