# island remover: find cells that are not connected to the edge

grid = [
	[0, 1, 0, 0, 0, 0],
	[0, 1, 0, 1, 0, 0],
	[0, 1, 1, 1, 0, 0],
	[0, 0, 0, 0, 1, 0],
	[0, 1, 0, 1, 0, 0],
	[0, 1, 0, 0, 0, 1],
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


def get_path(grid, i, j):
	visited = set()
	stack = [[i, j]]

	while len(stack) > 0:
		node = stack.pop()

		neighbors = get_populated_neighbors(grid, *node)

		#list comp?
		for neighbor in neighbors:
			if neighbor not in visited:
				stack.append(neighbor)
				visited.add(neighbor)

	return visited


for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == 1:
			print(get_path(grid, i, j))



