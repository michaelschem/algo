grid = [
['b','b','y','r'],
['b','g','r','g'],
['r','g','g','g']
]

colors = []
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] not in colors:
			colors.append(grid[i][j])

# grid_vals = [[[0]*len(colors)]*len(grid[0])]*len(grid)

grid_vals = [[[0 for _ in range(len(colors))] for _ in range(len(grid[0]))] for _ in range(len(grid))]


def print_grid(grid):
	for line in grid:
		print(line)

print(colors)
print_grid(grid_vals)
print_grid(grid)

def get_same_neighbors_count(color, i, j, c):
	count = 0

	if grid[i][j] == color:
		count += 1

	try:
		if grid[i+1][j] == color:
			count += 1
	except IndexError:
		pass

	try:
		if grid[i][j+1] == color:
			count += 1
	except IndexError:
		pass

	return count #+ grid_vals[i][j][c]

# visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

def get_all_neighbors_count(color, i, j, c, visited=None):
	if grid[i][j] != color:
		return 0

	if visited == None:
		visited = [[i, j]]
	else:
		visited.append([i, j])

	count = 0
	try:
		if grid[i+1][j] == color:
			count += 1
			if [i+1, j] not in visited:
				count += get_all_neighbors_count(color, i+1, j, c, visited)
	except IndexError:
		pass

	try:
		if grid[i][j+1] == color:
			count += 1
			if [i, j+1] not in visited:
				count += get_all_neighbors_count(color, i, j+1, c, visited)
	except IndexError:
		pass

	try:
		if grid[i-1][j] == color:
			count += 1
			if [i-1, j] not in visited:
				count += get_all_neighbors_count(color, i-1, j, c, visited)
	except IndexError:
		pass

	try:
		if grid[i][j-1] == color:
			count += 1
			if [i, j-1] not in visited:
				count += get_all_neighbors_count(color, i, j-1, c, visited)
	except IndexError:
		pass

	return count

for i,_ in enumerate(grid_vals):
	for j,_ in enumerate(grid_vals[i]):
		for c,color in enumerate(colors):
			grid_vals[i][j][c] = get_all_neighbors_count(color, i, j, c)
			# print_grid(grid_vals)
			# print()

print_grid(grid_vals)


# for c,color in enumerate(colors):
# 	for i in len(grid):
# 		for j in len(grid[i]):
# 			if grid_vals[i][j][c] > 0:

