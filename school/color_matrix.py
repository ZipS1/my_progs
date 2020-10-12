def print_matrix():
    print()
    for i in matrix:
        print(i)
    print()

from random import randint as rand
matrix_height = 5
matrix_width = 5
value_from = 1
value_to = 3
repeat_possible = True
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

print_matrix()
start_point = input("Enter starting point (x, y): ").split()
start_point = [int(i) - 1 for i in start_point]
start_x, start_y = start_point


color = matrix[start_y][start_x]
new_color = int(input("Enter your color (0-3): "))
if color == new_color:
    print_matrix()

c_point = (start_y, start_x)

area = [c_point]

while True:
    y = c_point[0]
    x = c_point[1]
    matrix[y][x] = new_color

    if x - 1 >= 0:
        if matrix[y][x - 1] == color:
            area.append((y, x - 1))
    if x + 1 <= 4:
        if matrix[y][x + 1] == color:
            area.append((y, x + 1))
    if y - 1 >= 0:
        if matrix[y - 1][x] == color:
            area.append((y - 1, x))
    if y + 1 <= 4:
        if matrix[y + 1][x] == color:
            area.append((y + 1, x))
    area.remove(c_point)

    if area == []:
        print_matrix()
        quit()
    else:
        c_point = area[0]







