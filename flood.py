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

def print_grid(grid):
	for line in grid:
		print(line)

print_grid(grid)

def get_neighbors(color, i, j):
	offsets = [[1,0], [0,1], [-1,0], [0,-1]]

	neighbors = []
	for offset in offsets:
		try:
			if grid[i+offset[0]][j+offset[1]] == color:# and [i+offset[0], j+offset[1]] not in visited:
					neighbors.append((color, i+offset[0], j+offset[1]))
		except IndexError:
			pass

	return neighbors

stack = []
visited = {}
max_len = 0

for i,_ in enumerate(grid):
	for j,color in enumerate(grid[i]):
		stack.append((grid[i][j],i,j))

print(stack)
while len(stack) > 0:
	c,i,j = stack.pop()

	neighbors = get_neighbors(c,i,j)

	input()
	print(visited)
	print(stack)
	if (i,j) not in visited:
		visited[i,j] = len(neighbors)

	unvisited_neighbors = [neighbor for neighbor in neighbors if (neighbor[0],neighbor[1]) not in visited]
	stack.extend(unvisited_neighbors)

print(visited)
print(max_len)
