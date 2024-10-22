def html_special_chars(data): 
    conversion_dictionary = {"<": "&lt;",">":"&gt;",'"':"&quot;","&":"&amp;"}
    converted_str = ""
    for char in data:
        if char in conversion_dictionary:
            converted_str += conversion_dictionary[char]
        else:
            converted_str += char
    return converted_str