class BST:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def insert(root,data):
        if root is None:
            return BST(data)

        if data<root.data:
            root.left=BST.insert(root.left,data)
        if data>root.data:
              root.right=BST.insert(root.right,data)
        return root
  
    def kth_level(self, k):
        if self is None:
            return
        if k == 0:
            print(self.data, end = " ")
        elif k != 0:
            if self.left:
                self.left.kth_level(k-1)
            if self.right:
                self.right.kth_level(k-1)
        else:
            print(f"level {k} out of bounds")

root = BST(5)
root.insert(3)
root.insert(7)
root.insert(2)
root.insert(4)
root.insert(6)
root.insert(8)

k = 2  
print(f"Nodes at level {k}:")
root.kth_level(k)