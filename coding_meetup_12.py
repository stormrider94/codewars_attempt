def find_admin(lst, lang):
    return list(filter(lambda x: x['githubAdmin'] == 'yes' and x['language'] == lang,lst))