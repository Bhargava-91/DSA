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
  
  def is_full(self):
    if self is None:
      return True
    if self.left is None and self.right is None:
        return True
    if self.left and self.right:
      return self.left.is_full() and self.right.is_full()
    
    return False
  
root = BST(5)
root.insert(3)
root.insert(7)
root.insert(2)
root.insert(4)
root.insert(6)
root.insert(8)

if root.is_full():
    print("The binary tree is full.")
else:
    print("The binary tree is not full.")
