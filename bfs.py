from typing import List

class Node:
    def __init__(self, id):
        self.id = id
        self.children = []
        self.distance = 0

    def __repr__(self):
        return str({self.id: self.children})

class Graph:
    def __init__(self, n):
        self.nodes = {i: [] for i in range(0, n)}

    def connect(self, x, y):
        self.nodes[x].append(self.nodes[y])

    def find_all_distances(self, s):
        distances = []
        to_check = [self.nodes[1]]
        depth = 0
        while(len(to_check) > 0):
            node = to_check.pop()
            # distances.append(node.distance)
            for child in node:
                # child.distance = node.distance + 6
                to_check.append(child)

        print(distances)
        return distances

nm = [[4, 2], [1, 2], [1, 3]]
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1, y-1)
    s = int(input())
    graph.find_all_distances(s-1)


# print(graph.nodes)

# print(bfs(nodes, 3))





