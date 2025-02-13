def max_matrix(m):
    max_value = 0
    for row in m:
        for v in row:
            if v > max_value:
                max_value = v

    return max_value

matrix = [
    [20, 26, 34],
    [4, 5, 12], 
    [8, 9, 10]
]
print(max_matrix(matrix))

# --------------------------
def min_matrix(m):
    min_value = m[0][0]
    for row in m:
        for v in row:
            if v < min_value:
                min_value = v

    return min_value

print(min_matrix(matrix))

# --------------------------
def infos_matrix(m):
    return sum([len(row) for row in m])

print(infos_matrix(matrix))

# --------------------------
def transpose_matrix(m):

    
    return [[row[i] for row in m] for i in range(len(m[0]))]

print(transpose_matrix(matrix))