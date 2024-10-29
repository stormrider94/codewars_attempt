def reverse_letter(st):
    st_non_alphs_omitted = "".join([char for char in st if char.isalpha()])
    return st_non_alphs_omitted[::-1]