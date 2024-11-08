# I don't know if there is a mistake in the kata but then they should have told us that 
# if the odd number you have to split other numbers into is odd and can't be splitted further
# they should have told us to return it
# I think they said it, they said the job is to split all even numbers
# that means that all the odd numbers should remain untouched
def split_all_even_numbers(numbers, way):
    print("This is the way" + " , " + str(way))
    if way == 0:
        odd_numbers_gotten = split_close(numbers)
    elif way == 1:
        odd_numbers_gotten = split_further(numbers)
    elif way == 2:
        odd_numbers_gotten = split_equal(numbers)
    elif way == 3:
        odd_numbers_gotten = split_ones(numbers)
    
    return odd_numbers_gotten
    
# if way == 0 
def split_close(nums):
    all_odds_totale = []
    for num in nums:
        if num % 2 == 1:
            all_odds_totale.append(num)
            continue
        split_odds = []
        if num == 1:
            all_odds_totale.append(1)
            continue
        for i in range(1,num):
            for j in range(num):
                # if both i and j are all odd numbers and i+j will give you num, add them to a list
                if i % 2 == 1 and j % 2 == 1 and i+j == num:
                    split_odds.append([i,j])
        # if the number can't be split but then it is also an odd number
        if len(split_odds) == 0 and num % 2 == 1:
            all_odds_totale.append(num)
        # if split_odds has just one value, we don't need to do the min or max thing
#         if len(split_odds) <= 1:
#             all_odds_totale.extend(sorted(split_odds))
#             continue
        min_li = split_odds[0]
        min_val  = abs(split_odds[0][0] - split_odds[0][1])
        for li in split_odds:
            a = li[0]
            b = li[1]
            if abs(a-b) < min_val:
                min_li = sorted([a,b])
                min_val = abs(a-b)
        all_odds_totale.extend(min_li)
    print(all_odds_totale)
    return all_odds_totale
    
# if way == 1
def split_further(nums):
    all_odds_totale = []
    for num in nums:
        if num % 2 == 1:
            all_odds_totale.append(num)
            continue
        split_odds = []
        if num == 1:
            all_odds_totale.append(1)
            continue
        for i in range(1,num):
            for j in range(num):
                # if both i and j are all odd numbers and i+j will give you num, add them to a list
                if i % 2 == 1 and j % 2 == 1 and i+j == num:
                    split_odds.append([i,j])
        if len(split_odds) == 0 and num % 2 == 1:
            all_odds_totale.append(num)
        # if split_odds has just one value, we don't need to do the min or max thing
#         if len(split_odds) <= 1:
#             all_odds_totale.extend(sorted(split_odds))
#             continue
        max_li = split_odds[0]
        max_val  = abs(split_odds[0][0] - split_odds[0][1])
        for li in split_odds:
            a = li[0]
            b = li[1]
            if abs(a-b) > max_val:
                max_li = sorted([a,b])
                max_val = abs(a-b)
        all_odds_totale.extend(max_li)
    print(all_odds_totale)
    return all_odds_totale

# if way == 2
def split_equal(nums):
    all_odds_totale = []
    for num in nums:
        if num % 2 == 1:
            all_odds_totale.append(num)
        else:
            split_odds = []
            for i in range(1,num+1):
                #if num is divisible by that number and that number is also an odd number
                if num % i == 0 and i % 2 == 1:
                    equal_num = i
                    n = num // i
            for i in range(n):
                split_odds.append(equal_num)
            all_odds_totale.extend(split_odds)
    return all_odds_totale

# if way == 3
def split_ones(nums):
    all_odds_totale = []
    for num in nums:
        if num % 2 == 1:
            all_odds_totale.append(num)
        else:
            split_odds = []
            for i in range(num):
                split_odds.append(1)
            all_odds_totale.extend(split_odds)
            
    return all_odds_totale
    


# we need to get two odd numbers that when you add you will get that number