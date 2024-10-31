def validate_hello(greetings):
    greetings_in_languages = ["hello","cia","salut","hallo","hola","ahoj","czesc"]
    for greeting in greetings_in_languages:
        if greeting in greetings.lower():
            return True
    return False