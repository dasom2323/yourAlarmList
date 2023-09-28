# Linked List for alarm links from txt file

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    # Instantiates a new list with default value
    def __init__(self):
        self.head = None
        self.last = None
        self.iterator = None

    # Add a new node at the beginning of the list
    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Add a new node at the end of the list
    def add_last(self, data):
        new_node = Node(data)
        new_node.next = None
        if self.head is None:
            self.last = new_node
            self.head = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node

    # Removes node at the beginning of the list
    def remove_first(self):
        if self.head is None:
            raise Exception("The list is empty.")
        elif self.head == self.last:
            self.head = None
            self.last = None
        else:
            if self.iterator == self.head:
                self.iterator = None
            self.head = self.head.next
            self.head.prev = None

    # Removes node at the end of the list
    def remove_last(self):
        if self.head is None:
            raise Exception("The list is empty.")
        elif self.head == self.last:
            self.head = None
            self.last = None
        else:
            if self.iterator == self.last:
                self.iterator = None
            self.last = self.last.prev
            self.last.next = None

    # Place iterator at the beginning of the list
    def place_iterator(self):
        self.iterator = self.head

    # Removes the node pointed by iterator
    def remove_iterator(self):
        if self.iterator is None:
            raise Exception("Iterator is null. Failed to remove.")
        elif self.iterator == self.head:
            self.remove_first()
        elif self.iterator == self.last:
            self.remove_last()
        else:
            self.iterator.prev.next = self.iterator.next
            self.iterator.next.prev = self.iterator.prev
        self.iterator = None

    # Add element after the node pointed by iterator
    def add_iterator(self, data):
        if self.iterator is None:
            raise Exception("Iterator is null. Failed to add.")
        elif self.iterator == self.last:
            self.add_last(data)
        else:
            new_node = Node(data)
            self.iterator.next.prev = new_node
            new_node.next = self.iterator.next
            self.iterator.next = new_node
            new_node.prev = self.iterator

    # Moves iterator up by 1 node
    def advance_iterator(self):
        if self.iterator is None:
            raise Exception("Iterator is null")
        self.iterator = self.iterator.next

    # Moves iterator down by 1 node
    def reverse_iterator(self):
        if self.iterator is None:
            raise Exception("Iterator is null")
        self.iterator = self.iterator.prev

    # Returns the data in the first node
    def get_first(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.head.data

    # Returns the data in the last node
    def get_last(self):
        if self.get_length() == 0:
            raise Exception("The list is empty.")
        return self.last.data

    # Check if the list is empty
    def is_empty(self):
        return self.get_length() == 0

    # Returns alarm title in the node pointed by iterator
    def get_iterator(self):
        if self.iterator is None:
            raise Exception("Iterator is null. Failed to get title.")
        return self.iterator.data

    # Returns the length of the list
    def get_length(self):
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length

    def print_numbered_list(self):
        temp = self.head
        num = 1
        while temp is not None:
            s = "{}. " + temp.data
            print(s.format(num))
            temp = temp.next
            num += 1
