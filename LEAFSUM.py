class BST:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(root, data):
        if root is None:
            return BST(data)
        
        if data<root.data:
            root.left=BST.insert(root.left,data)
        if data>root.data:
            root.right=BST.insert(root.right,data)
        return root
    
    def sumleaf(root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        
        leftsum = root.left.sumleaf() if root.left else 0
        rightsum = root.right.sumleaf() if root.right else 0

        return leftsum + rightsum
        
    
root = BST(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
root.insert(12)
root.insert(18)

sum_of_leaf_nodes = root.sumleaf()
print(f"Sum of leaf nodes: {sum_of_leaf_nodes}")