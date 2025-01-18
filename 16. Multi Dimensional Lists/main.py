# Multi Dimensional Lists
# a list of lists (Matrix) 
matrix = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10]
]

print(matrix[1][3])

matrix [0][1] = 55
print(matrix)
print("------------")

# looping
def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end=' ')
        print()

print_matrix(matrix)
print("------------")

print([[x*2 for x in row] for row in matrix])
