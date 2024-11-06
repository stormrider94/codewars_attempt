def solution(number):
    multiples_li = []
    for i in range(2,number):
        if i%3==0 and i%5 ==0:
            multiples_li.append(i)
        elif i%3==0:
            multiples_li.append(i)
        elif i % 5 == 0:
            multiples_li.append(i)
    return sum(multiples_li)