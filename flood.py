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

grid_vals = {}

def print_grid(grid):
	for line in grid:
		print(line)

print_grid(grid)

def get_all_neighbors_count(color, i, j, visited=None):
	offsets = [[1,0], [0,1], [-1,0], [0,-1]]

	if visited == None:
		visited = [[i, j]]
	else:
		visited.append([i, j])

	for offset in offsets:
		try:
			if grid[i+offset[0]][j+offset[1]] == color:
				if [i+offset[0], j+offset[1]] not in visited:
					visited = get_all_neighbors_count(color, i+offset[0], j+offset[1], visited)
		except IndexError:
			pass

	return visited

for i,_ in enumerate(grid):
	for j,color in enumerate(grid[i]):
		if grid[i][j] == color:
			grid_vals[i,j,color] = len(get_all_neighbors_count(color, i, j))

print(grid_vals)

