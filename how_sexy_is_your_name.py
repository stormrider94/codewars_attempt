SCORES = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
          'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
          'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
          'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}

def sexy_name(name):
    score = sum([SCORES.get(letter.upper()) for letter in name if letter != " "]) if name else -1
    if score <= 60:
        return 'NOT TOO SEXY'
    elif score >= 61 and score <= 300:
        return 'PRETTY SEXY'
    elif score >= 301 and score <= 599:
        return 'VERY SEXY'
    else:
        return 'THE ULTIMATE SEXIEST'