'''
Implement a linked list
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            return
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def insert_front(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = newnode
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, prev_node, new_data):
        new_node = Node(new_data)
        if prev_node is None:
            print("Previous node is absent!")
            return
        else:
           new_node.next = prev_node.next
           prev_node.next = new_node

    def insert_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def reverse(self):
        if self.head is None:
            return None
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

if __name__ == '__main__':

    llist = LinkedList()
    llist.insert_end(1)
    llist.print_list()
    llist.insert_end(2)
    llist.insert_end(3)
    llist.insert_after(llist.head.next.next, 4)
    llist.insert_end(5)
    llist.insert_front(0)
    llist.print_list()
    llist.reverse()
    llist.print_list()



