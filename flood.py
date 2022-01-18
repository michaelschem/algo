grid = [
	['b','b','y','r'],
	['b','g','r','g'],
	['r','g','g','g']
]

def print_grid(grid):
	for line in grid:
		print(line)

print_grid(grid)

class Node():
	def __init__(self,c,i,j,visited):
		self.c = c
		self.i = i
		self.j = j
		visited[i,j] = None
		self.visited = visited

	@property
	def unvisited_neighbors(self):
		offsets = [[1,0], [0,1], [-1,0], [0,-1]]

		neighbors = []
		for offset in offsets:
			x,y = self.i+offset[0],self.j+offset[1]
			try:
				if grid[x][y] == self.c:
					if (x, y) not in self.visited:
						neighbors.append(Node(color, x, y,visited))
			except IndexError:
				pass

		return neighbors

tree_lens = {}
max_len = 0

for i,_ in enumerate(grid):
	for j,color in enumerate(grid[i]):
		stack = []
		visited = {}
		stack.append(Node(grid[i][j],i,j,visited))

		while len(stack) > 0:
			node = stack.pop()

			neighbors = node.unvisited_neighbors

			stack.extend(neighbors)

		max_len = max(max_len, len(visited))
		tree_lens[i,j] = len(visited)

print(tree_lens)
print(max_len)
