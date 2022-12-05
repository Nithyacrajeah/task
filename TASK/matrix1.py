# Print the matrix filled with consequtive numbers starting from one(1)
# 3x4
# 3x3


a = int(input("Enter number of Rows"))
b = int(input("Enter number of Columns"))
matrix = []
for i in range(a):
    c =  []
    for j in range(b):
        k=int(input())
        c.append(k)
    matrix.append(c)
for i in range(a):
    for j in range(b):
        print(matrix[i][j], end = " " )
    print()