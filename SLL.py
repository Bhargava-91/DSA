class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.top
        self.top = newnode
        print(f"Pushed {data} onto the stack")

    def pop(self):
        if self.top is None:
            print("list is empty")

        pop_data = self.top.data
        self.top = self.top.next
        print(f"popped {pop_data} from stack")
    
    def peek(self):
        if self.top is None:
            print("list is empty")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def display(self):
        if self.is_empty():
            print("list is empty")
        else:
            temp = self.top
            while temp is not None:
                print(temp.data)
                temp = temp.next
                
    def size(self):
        if self.is_empty():
            return 0
        else:
            size = 0
            temp = self.top
            while temp is not None:
                size += 1
                temp = temp.next
        return f"size : {size}"
    


s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)

s1.display()

print(s1.size())

s1.pop()
s1.display()