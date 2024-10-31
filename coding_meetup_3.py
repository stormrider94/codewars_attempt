def is_ruby_coming(lst):
    return any(developer['language'] == 'Ruby' for developer in lst)