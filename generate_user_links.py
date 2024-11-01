import urllib.parse
def generate_link(user):
    prefix = "http://www.codewars.com/users/"
    encoded_user = urllib.parse.quote(user)
    return prefix + encoded_user