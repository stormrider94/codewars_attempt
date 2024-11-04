def matrix_elements_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                continue
            elif (i != 0) and (0 in [matrix[num][j] for num in range(0,i)]):
                continue
            sum += matrix[i][j]
    print(matrix)
    print(sum)
    return sum
    
#     if there is zero in any of the indices at the top 