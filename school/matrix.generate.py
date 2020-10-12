from random import randint as rand

def print_matrix():
    print()
    for i in matrix:
        print(i)
    print()

def generateMatrix(matrix_height, matrix_width, value_from, value_to, repeat_possible):
#--------------MATRIX GENERATION----------------------------
if not repeat_possible:
    if value_to - value_from + 1 < matrix_height*matrix_width:
        print('Некорректная настройка матрицы!')
        quit()
matrix = []
row = []
elements = []
for r in range(matrix_height):
    row = []
    for i in range(matrix_width):
        a = rand(value_from, value_to)
        if not repeat_possible:
            while a in elements:
                a = rand(value_from, value_to)
        row.append(a)
        elements.append(a) 
    matrix.append(row)
#-----------------------------------------------------------