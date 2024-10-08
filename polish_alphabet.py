def correct_polish_letters(st):
    diacritics_dict = {"ą":"a","ć":"c","ę":"e","ł":"l","ń":"n","ó":"o","ś":"s","ź":"z",'ż':"z"}
    corrected_str = ""
    for x in st:
        if x in diacritics_dict:
            corrected_str += diacritics_dict[x]
        else:
            corrected_str += x
    return corrected_str