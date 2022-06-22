class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    # def __repr__(self):
    #     return str({self.info: [self.left, self.right]})

    def __repr__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

from collections import deque

def levelOrder(root):
    depth = -1
    next_level = deque([root])
    order = []
    while (next_level):
        to_visit = deque([*next_level])
        next_level = deque([])
        depth += 1
        while (len(to_visit) > 0):
            current = to_visit.popleft()
            order.append(current)

            if current.left:
                next_level.append(current.left)

            if current.right:
                next_level.append(current.right)



    print(*order)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)