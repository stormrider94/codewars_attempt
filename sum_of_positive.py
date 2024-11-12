def positive_sum(arr):
    # Your code here
    sum=0
    for number in arr:
        if number>0:
            sum=number + sum          
    return sum