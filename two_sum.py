def two_sum(numbers, target):
    mysterio = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] == target:
                mysterio.append(i)
                mysterio.append(j)
                return mysterio
                break
    
    
    
    # be careful about indentation rules in python