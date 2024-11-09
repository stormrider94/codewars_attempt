def sort_twisted37(arr):
    # we need to first replace all the "3"s and "7"s with their replacements
    # after that we sort the list of replaced values
    #after that we replace the replaced list with their original "7"s and "3"s
    same_arr=arr
    switched_li=[]
    switched_again_li=[]
    for num in same_arr:
        numStr=str(num)
        if ("3" in numStr) or ("7" in numStr):
            replacedStr=numStr.replace('3', '%temp%').replace('7', '3').replace('%temp%', '7')
            switched_li.append(int(replacedStr))
        else:
            switched_li.append(num)
    sorted_li=sorted(switched_li)
    print(arr,sorted_li)
    for num in sorted_li:
        numStr=str(num)
        if "3" in numStr or "7" in numStr:
            replacedStr=numStr.replace('3', '%temp%').replace('7', '3').replace('%temp%', '7')
            switched_again_li.append(int(replacedStr))
        else:
            switched_again_li.append(num)
    print(switched_again_li)
    return switched_again_li