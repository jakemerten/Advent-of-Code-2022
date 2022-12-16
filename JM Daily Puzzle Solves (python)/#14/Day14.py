import numpy as np

with open("day14input.txt") as reader:
	lines = reader.readlines()

puzzle = []
for line in lines:
	line = line.strip()
	line = line.split()
	for x in range(0,len(line)-2,2):
		start = line[x].split(',')
		end = line[x+2].split(',')
		row = [start,end]
		puzzle.append(row)


smallest_x = 500
largest_x = 500

largest_y = 0
smallest_y = 0

for line in puzzle:
	for element in line:
		x = int(element[0])
		y = int(element[1])
		if x > largest_x:
			largest_x = x
		if x < smallest_x:
			smallest_x = x
		if y > largest_y:
			largest_y = y
		if y < smallest_y:
			smallest_y = y

if smallest_y != 0:
	print("check smallest y")

total_columns = 1000
total_rows = largest_y - smallest_y + 1+2
x_offset = smallest_x

grid = []
for x in range(total_rows):
	row = []
	for y in range(total_columns):
		row.append('.')
	grid.append(row)

start = (500,0)
end = (smallest_x, largest_y -1)
end = False

grid[start[1]][start[0]] = "+"

for line in puzzle:
	start_point = line[0]
	end_point = line[1]
	start_x = int(start_point[0]) 
	start_y = int(start_point[1])
	end_x = int(end_point[0]) 
	end_y = int(end_point[1])

	if (start_x != end_x) and (start_y != end_y):
		print("Error: not horizontal or vertical line")

	smaller_x = min(start_x,end_x)
	larger_x = max(start_x,end_x)
	smaller_y = min(start_y,end_y)
	larger_y = max(start_y,end_y)

	for y in range(smaller_y, larger_y+1):
		for x in range(smaller_x,larger_x+1):
			grid[y][x]="#"

for x in range(total_columns):
	grid[total_rows - 1][x] = "#"

print(total_rows)
print(total_columns)

print(np.array(grid))

def drop_sand():
	global end
	at_rest = False
	position = start
	while at_rest == False:
		if at_rest == False:
			current_x = position[0]
			current_y = position[1]
			down = (current_x,current_y + 1)
			left_down = (current_x - 1, current_y+1)
			right_down = (current_x + 1, current_y + 1)
			if grid[down[1]][down[0]] == ".":
				position = down
			elif grid[left_down[1]][left_down[0]] == '.':
				position = left_down
			elif grid[right_down[1]][right_down[0]] == ".":
				position = right_down
			else:
				grid[current_y][current_x] = "s"
				if current_x == 500 and current_y == 0:
					end = True
				at_rest = True
		

count = 0
while end == False:
	count += 1
	drop_sand()
	
print(count-1)


print(np.array(grid))