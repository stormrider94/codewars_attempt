def order(sentence):
  # code here
    import re
    string_arr= sentence.split(" ")
    sorted_arr=sorted(string_arr,key=lambda word: re.findall("\d",word))
    print(string_arr, sorted_arr)
    str=" "
    final_result=str.join(sorted_arr)
    print(final_result)
    return final_result