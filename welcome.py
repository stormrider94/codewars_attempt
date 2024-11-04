language_greeting_pairings = [ ("english", "Welcome")
, ("czech", "Vitejte")
, ("danish", "Velkomst")
, ("dutch", "Welkom")
, ("estonian", "Tere tulemast")
, ("finnish", "Tervetuloa")
, ("flemish", "Welgekomen")
, ("french", "Bienvenue")
, ("german", "Willkommen")
, ("irish", "Failte")
, ("italian", "Benvenuto")
, ("latvian", "Gaidits")
, ("lithuanian", "Laukiamas")
, ("polish", "Witamy")
, ("spanish", "Bienvenido")
, ("swedish", "Valkommen")
, ("welsh", "Croeso")
]

def greet(language):
    languages = [pair[0] for pair in language_greeting_pairings]
    if language in languages:
        idx = languages.index(language)
        return language_greeting_pairings[idx][1]
    idx = languages.index("english")
    return language_greeting_pairings[idx][1]