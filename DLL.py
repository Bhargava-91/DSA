class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        new_node =  Node(data)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            new_node.prev = temp_node
            temp_node.next = new_node

    def addafter(self, data, x):
        if self.head is None:
            print("Ll is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("Element not found")
            else:
                newnode = Node(data)
                newnode.next = n.next
                newnode.prev = n
                if n.next is not None:
                    n.next.prev = newnode
                    n.next = newnode
                
    def addbefore(self, data, x):
        if self.head is None:
            print("Ll is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("Element not found")
            else:
                newnode = Node(data)
                newnode.prev = n.prev
                if n.prev is not None:
                    n.prev.next = n
                else:
                    self.head = newnode
                    n.prev = newnode

    def insert_at_pos(self, data, pos):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            if pos == 1:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                c = 1
                temp_node = self.head

                while c<pos -1:
                    temp_node = temp_node.next
                    c += 1

                if temp_node is None:
                    print("Position out of bounds")
                    return
                print(f"Inserting {new_node.data} at {pos}")
                new_node.next = temp_node.next
                new_node.prev = temp_node
                temp_node.next.prev = new_node
                temp_node.next = new_node

    def delete_at_beg(self):
        if self.head is None:
            print("List is Empty")
        else:
            print(f"\n deleted {self.head.data} from beg")
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp_node1 = self.head
            temp_node2 = None

            while temp_node1.next is not None:
                temp_node2 = temp_node1
                temp_node1 = temp_node1.next

            print(f"\n deleted last node {temp_node1.data}")                    
            temp_node2.next = None

    def delbyval(self, x):
        if self.head is None:
            print("DLL is Empty")
            return

        if self.head.data == x:
            if self.head.next is None:
                    self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("Value not found in DLL")
        else:
            if n.next is not None:
                n.next.prev = n.prev
            if n.next is None:
                n.prev.next = n.next

    def del_at_pos(self, pos):
        if self.head is None:
            print("List is Empty")

        else:

            if pos == 1:
                self.head = self.head.next
                self.head.prev = None

            else:
                c = 1
                temp_node1 = self.head
                temp_node2 = None
                while c < pos - 1:
                    temp_node2 = temp_node1
                    temp_node1 = temp_node1.next
                    c += 1

                if temp_node1 is None:
                    print("position out of bounds")
                    return
                else:
                    temp_node1.prev = None
                    temp_node2.next = temp_node1.next
                    temp_node1.next.prev = temp_node2
                    temp_node1.next = None

    def ftraverse(self):
        print('\n forward traverse')
        if self.head is None:
            print("List is Empty")
        else:
            tempnode = self.head
            while tempnode is not None:
                print(tempnode.data)
                tempnode = tempnode.next
    
    def btraverse(self):
        print("\n backward traverse")
        if self.head is None:
            print("List is Empty")
        else:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            while temp_node is not None:
                print(temp_node.data)
                temp_node = temp_node.prev


dll=DLL()
dll.head=Node(10)
n2=Node(20)
n3=Node(30)

dll.head.next=n2
n2.next=n3
n2.prev=dll.head
n3.prev=n2


dll.insert_at_beg(1)

dll.insert_at_end(40)
dll.insert_at_pos(15,2)
dll.addafter(30,10)
dll.addbefore(20,11)
dll.ftraverse()
dll.btraverse()

dll.del_at_pos(3)
dll.ftraverse()
dll.btraverse()

dll.delete_at_beg()
dll.ftraverse()
dll.btraverse()
dll.delete_at_end()

dll.ftraverse()
dll.btraverse()