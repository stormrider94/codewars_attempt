import re
def to_camel_case(text):
    if not text:
        return ""
    camel_case_li_to_join = []
    word_li = re.split('-|_',text)
    print(word_li)
    if word_li[0][0].isupper():
        camel_case_li_to_join.append(word_li[0])
    else:
        camel_case_li_to_join.append(word_li[0])
    for word in word_li[1:]:
        camel_case_li_to_join.append(word.capitalize())
    return ''.join(camel_case_li_to_join)