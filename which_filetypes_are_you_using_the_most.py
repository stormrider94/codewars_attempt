def solve(files):
    if not files:
        return []
    dict = {}
    extensions = []
    for file in files:
        file_ext_split = file.split('.')
        if len(file_ext_split[1:]) > 1:
            # we get the last index
            extension_name = file_ext_split[len(file_ext_split)-1]
        else:
            extension_name = file_ext_split[1]
        extensions.append(extension_name)

    all_extensions = sorted(list(set(extensions)))
    dict = {}
    for ext in all_extensions:
        dict[ext] = extensions.count(ext)
    sorted_items = sorted(dict.items(),key=lambda x : x[1],reverse = True)
    max_filetype_value = sorted_items[0][1]
    most_common_filetypes = []
    for item in sorted_items:
        if item[1] == max_filetype_value:
            most_common_filetypes.append(f".{item[0]}")
    print(most_common_filetypes)
    return most_common_filetypes