def print_matrix():
    print()
    for i in matrix:
        print(i)
    print()

from random import randint as rand
matrix_height = 5
matrix_width = 5
value_from = 0
value_to = 1
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
WIDTH = len(matrix[0])
HEIGHT = len(matrix)
y_m = 0
x_m = 0
terr_cells = []
islands_amount = 0
for i in matrix:
    x_m = 0
    for cell  in i:
        if cell == 1 and (y_m, x_m) not in terr_cells:
            c_point = (y_m, x_m)
            area = [c_point]

            while True:
                y = c_point[0]
                x = c_point[1]
                terr_cells.append((y, x))

                if x - 1 >= 0:
                    if matrix[y][x - 1] == 1 and (y, x - 1) not in terr_cells:
                        area.append((y, x - 1))
                if x + 1 <= WIDTH - 1:
                    if matrix[y][x + 1] == 1 and (y, x + 1) not in terr_cells:
                        area.append((y, x + 1))
                if y - 1 >= 0:
                    if matrix[y - 1][x] == 1 and (y - 1, x) not in terr_cells:
                        area.append((y - 1, x))
                if y + 1 <= HEIGHT - 1:
                    if matrix[y + 1][x] == 1 and (y + 1, x) not in terr_cells:
                        area.append((y + 1, x))
                area.remove(c_point)

                if area == []:
                    islands_amount += 1
                    break
                else:
                    c_point = area[0]
        x_m += 1
    y_m += 1

print("MATRIX".center(matrix_width*3, "-"))
print_matrix()
print("Островов: ", islands_amount)



