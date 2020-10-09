import random

matrix = [[0,1,0,1,1],
		  [1,1,1,2,2],
		  [0,1,0,2,2],
		  [3,3,1,2,2],
		  [0,1,1,0,0]]

# matrix[y][x]

start_point = input("Enter starting point (x, y): ").split()
start_point = [(int(i) - 1) for i in start_point]
start_x, start_y = start_point

color = matrix[start_y][start_x]
new_color = 2
c_point = [start_y, start_x]

area = [c_point]

while True:
	matrix[c_point[0]][c_point[1]] = new_color
	












#color point
#delete from area list 
#find "our" color in near points (m.b. with func)
#add them to area list