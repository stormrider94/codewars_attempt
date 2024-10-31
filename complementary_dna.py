def DNA_strand(dna):
    final_str = ""
    for letter in dna:
        if letter == "A":
            final_str += "T"
        elif letter == "T":
            final_str += "A"
        elif letter == 'C':
            final_str += "G"
        elif letter == 'G':
            final_str += 'C'
        else:
            final_str += letter
    return final_str