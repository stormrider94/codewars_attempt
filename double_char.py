def double_char(s):
    output_str = ""
    for letter in s:
        output_str+=letter
        output_str+=letter
    print(f"{s},{output_str}")
    return output_str