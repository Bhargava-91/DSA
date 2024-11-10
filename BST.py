class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def inorder(root):
        if root:
            BST.inorder(root.left)
            print(root.data, end = " ")
            BST.inorder(root.right)

    def insert(root, data):
        if root is None:
            return BST(data)
        
        if data < root.data:
            root.left = BST.insert(root.left, data)
        if data > root.data:
            root.right = BST.insert(root.right, data)
        return root
    
    def insert1(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left  = BST(data)
                else:
                    self.left.insert1(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BST(data)
                else:
                    self.right.insert1(data)
            else:
                self.data = data

    def findval(self, val):
        if val < self.data:
            if self.left is None:
                return str(val) + " not found"
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + " not found"
            return self.right.findval(val)
        else:
            print(str(self.data)  + ' is found')

def minvaluenode(root):
    current = root
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root, data):
    if root is None:
        return root
    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif (data > root.data):
        root.right = deleteNode(root.right, data)
    else:
        if root.left is None:
            temp  = root.right
            root = None
            return temp
        elif root.right is None:
            temp  = root.left
            root = None
            return temp
        
        temp = minvaluenode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

root = BST(50)
root.insert(30)
root.insert(20)
root.insert(40)
root.insert(70)
root.insert(60)
root.insert(80)

# print(root.findval(40))  
print(root.findval(100))  

root.inorder()
print()

root = deleteNode(root, 20)
print(root.findval(20))

root.inorder()