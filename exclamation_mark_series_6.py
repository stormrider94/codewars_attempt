def remove(st, n):
    new_st = ""
    count_n = 0
    number_of_exclamation_marks = st.count('!')
    if n >= number_of_exclamation_marks:
        for letter in st:
            if letter != '!':
                new_st += letter
    elif n<number_of_exclamation_marks:
        for letter in st:
            if letter == '!' and count_n != n:
                count_n += 1
            elif letter != '!' or (letter == '!' and count_n == n):
                new_st += letter
                
    return new_st