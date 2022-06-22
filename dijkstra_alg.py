import math
from collections import deque


class Edge:
    def __init__(self, distance, to):
        self.distance = distance
        self.to = to

    def __repr__(self):
        return f"{self.distance}->{self.to}"

class Node:
    def __init__(self):
        self.distance = math.inf
        self.edges = []

    def __repr__(self):
        return f"{self.distance}: {self.edges}"



class DGraph:
    def __init__(self, edges, nodes):
        self.visited = []
        self.unvisited = {node: Node() for node in nodes}
        for (k1, k2), distance in edges.items():
            self.unvisited[k1].edges.append(Edge(distance, k2))
            self.unvisited[k2].edges.append(Edge(distance, k1))

        self.distances = {edge for edge in edges}


    def set_weights(self, start='a'):
        self.unvisited[start].distance = 0
        self.visited.append(start)

        path = [start]
        for key, node in self.unvisited.items():
            for edge in node.edges:
                if self.unvisited[edge.to].distance > node.distance + edge.distance:
                    self.unvisited[edge.to].distance = node.distance + edge.distance

            # get path
            options = [(a,b.distance) for a,b in self.unvisited.items()]
            options.sort(key=lambda x: x[1])

            for option in options:
                if option[0] not in self.visited and option[0] in [a.to for a in self.unvisited[path[-1]].edges]:
                    path.append(option[0])
                    self.visited.append(option[0])
                    break


        return path

    def traverse(self, start='a', end='g'):
        current = start
        path = [start]

        while current != end:
            self.visited[current] = self.unvisited.pop(current)
            options = []
            for node in self.visited[current].edges:
                if node.to in self.visited:
                    continue
                options.append((node.to, self.unvisited[node.to].distance))
            options.sort(key=lambda x: x[1])
            current, _ = options[0]
            path.append(current)


        return path

edges = {
    ("a", "b"): 4,
    ("a", "c"): 3,
    ("a", "e"): 7,
    ("b", "c"): 6,
    ("b", "d"): 5,
    ("e", "c"): 8,
    ("e", "d"): 2,
    ("e", "g"): 5,
    ("g", "d"): 10,
    ("d", "f"): 2,
    ("f", "g"): 3
}

nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

dgraph = DGraph(edges, nodes)
path = dgraph.set_weights()
print(path)
# path = dgraph.traverse()
# print(path)
