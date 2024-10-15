def shortcut( s ):
    return "".join([ letter if letter  not in "aeiou" else ""  for letter in s])