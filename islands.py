# island remover: find cells that are not connected to the edge

grid = [
	#0,0            0,len(grid[0])
	[0, 1, 0, 0, 0, 0],
	[0, 1, 0, 1, 0, 0],
	[0, 1, 1, 1, 0, 0],
	[0, 0, 0, 0, 1, 0],
	[0, 1, 0, 1, 0, 0],
	[0, 1, 0, 0, 0, 1],
	#len(grid),0    len(grid), len(grid[0])
]

def get_populated_neighbors(grid, i, j):
	offsets = [[-1,0], [0,-1], [1, 0], [0,1]]

	neighbors = [(i, j)]
	for offset in offsets:
		x = i+offset[0]
		y = j+offset[1]
		if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
			if grid[x][y] == 1:
				neighbors.append((x, y))

	return neighbors


def get_path(grid, stack):
	visited = set()

	while len(stack) > 0:	
		node = stack.pop()

		neighbors = get_populated_neighbors(grid, *node)

		#list comp?
		for neighbor in neighbors:
			if neighbor not in visited:
				stack.add(neighbor)
				visited.add(neighbor)

	return visited

def get_edges(grid):
	edges = set()
	# 0,0 -> 0,len(grid[0])
	for i in range(0, len(grid)):
		if grid[0][i] == 1:
			edges.add((0,i))
	# 0,len(grid[0]) -> len(grid),len(grid[0])
	for i in range(0, len(grid)):
		if grid[i][len(grid[0])-1] == 1:
			edges.add((i,len(grid[0])-1))
	# len(grid), len(grid[0]) -> len(grid),0
	for i in range(0, len(grid[0])):
		if grid[len(grid)-1][i] == 1:
			edges.add((len(grid)-1,i))
	# len(grid),0 -> 0,0
	for i in range(0, len(grid)):
		if grid[len(grid)-1][i] == 1:
			edges.add((len(grid)-1,i))

	return edges



edges = get_edges(grid)

non_islands = get_path(grid, edges)

print(non_islands)

for i in grid:
	print(i)

print()

for i,_ in enumerate(grid):
	for j,val in enumerate(grid[i]):
		if (i,j) not in non_islands:
			grid[i][j] = 0


for i in grid:
	print(i)




