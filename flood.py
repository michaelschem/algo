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
	def __init__(self,color,i,j):
		print(color,i,j)
		if type(i) != int and type(j) != int:
			raise ValidationError()
		self.color = color
		self.i = i
		self.j = j

	@property
	def neighbors(self):
		offsets = [[1,0], [0,1], [-1,0], [0,-1]]

		neighbors = []
		for offset in offsets:
			x,y = self.i+offset[0],self.j+offset[1]
			try:
				if grid[x][y] == self.color:
					neighbors.append(Node(self.color, x, y))
			except IndexError:
				pass

		return neighbors

	def __repr__(self):
		return f"<Node ({self.color}, {self.i}, {self.j})>"

# node = Node('b',0,0)
# print(node.neighbors)

tree_lens = {}
max_len = 0

for i,_ in enumerate(grid):
	for j,color in enumerate(grid[i]):
		stack = [Node(grid[i][j],i,j)]
		visited = {}

		while len(stack) > 0:
			node = stack.pop()

			input()
			print("stack: ",stack)
			print("visited: ",visited)
			print("neighbors: ",node.neighbors)
			print((node,j))

			
			visited[(node.i, node,j)] = None

			# unvisited_neighbors = [neighbor for neighbor in node.neighbors if (neighbor.i,neighbor.j) not in visited]

			for neighbor in node.neighbors:
				if (neighbor.i, neighbor.j) not in visited:
					stack.append(neighbor)


		max_len = max(max_len, len(visited))
		tree_lens[i,j] = len(visited)

print(tree_lens)
print(max_len)
