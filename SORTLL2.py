class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def bubble_sort(self):
        if self.head is None:
            return
        end = None
        while end != self.head:
            temp = self.head
            while temp.next != end:
                if temp.data > temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                temp = temp.next
            end = temp

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert_at_end(5)
ll.insert_at_end(1)
ll.insert_at_end(4)
ll.insert_at_end(2)
ll.insert_at_end(3)

print("Original List:")
ll.display()

# Sorting the linked list
ll.bubble_sort()

print("\nSorted List:")
ll.display()