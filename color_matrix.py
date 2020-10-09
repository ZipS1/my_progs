def matrix_output():
	for i in matrix:
		print(i)
	quit()

import random

matrix = [[0,1,0,1,1],
		  [1,1,1,2,2],
		  [0,1,0,2,2],
		  [3,3,1,2,2],
		  [0,1,1,0,0]]

# matrix[y][x]

start_point = input("Enter starting point (x, y): ").split()
start_point = [int(i) - 1 for i in start_point]
start_x, start_y = start_point


color = matrix[start_y][start_x]
new_color = int(input("Enter your color (0-3): "))
if color == new_color:
	matrix_output()

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
		matrix_output()
	else:
		c_point = area[0]







