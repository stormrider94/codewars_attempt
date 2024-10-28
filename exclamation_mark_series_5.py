import re
def remove(st):
    all_ending_exclamation_marks_removed = []
    ends_with_exclamation_reg = re.compile(r'(!)+$')
    for word in st.split():
        all_ending_exclamation_marks_removed.append(ends_with_exclamation_reg.sub('',word))
    return ' '.join(all_ending_exclamation_marks_removed)