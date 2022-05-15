def output():
    matrix = [[0 for j in range(15)] for i in range(15)]

    matrix[6][7] = -1
    matrix[7][6] = -1
    matrix[8][7] = -1
    matrix[7][7] = 1
    matrix[8][5] = 1
    matrix[9][8] = 1
    print(matrix)


output()
