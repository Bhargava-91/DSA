class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BT:
    def __init__(self, root):
        self.root = root

    def nodes(self, root):
        if root is None:
            return 0
        return 1 + self.nodes(root.left) + self.nodes(root.right)
    
    def leafs(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.leafs(root.left) + self.leafs(root.right)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

tree = BT(root)

total_nodes = tree.nodes(root)
print(f"Total number of nodes: {total_nodes}")

leaf_nodes = tree.leafs(root)
print(f"Number of leaf nodes: {leaf_nodes}")