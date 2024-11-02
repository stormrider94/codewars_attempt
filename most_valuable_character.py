def solve(st):
    max_char = ''
    max_value = -1
    for letter in sorted(set(st)):
        first_index = st.index(letter)
        last_index = st.rindex(letter)
        position_diff = last_index - first_index
        
        if(position_diff > max_value) or (position_diff == max_value and letter < max_char):
            max_char = letter
            max_value = position_diff
    return max_char
        