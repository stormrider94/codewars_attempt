import re

def uncollapse(digits):
    digits_li = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    final_li = []
    index = 0
    for i in range(len(digits)):
        if digits[index:i+1] in digits_li:
            final_li.append(digits[index:i+1])
            if i != len(digits):
                index = i+1
    print(" ".join(final_li))                  
    return " ".join(final_li)