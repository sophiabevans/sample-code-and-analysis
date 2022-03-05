"""
Linked List Stack data structure
"""
from node import Node


class Stack:
    '''LIFO linked list'''

    def __init__(self, capacity):
        '''Create a Stack with capacity > 0 or defaultCapacity'''
        #check for valid capacity input, else use defaultCapacity
        if not type(capacity) == int:
            print("Capacity must be an integer > 0\nDefault capacity used")
            capacity = defaultCapacity
        if capacity <= 0:
            print("Capacity must be an integer > 0\nDefault capacity used")
            capacity = defaultCapacity
        self.head = None
        self.maxSize = capacity
        self.currentSize = 0

    def isEmpty(self):
        '''Return boolean indicating whether Stack is empty'''
        return self.currentSize == 0

    def isFull(self):
        '''Return boolean indicating whether Stack is full'''
        return self.currentSize == self.maxSize

    def push(self, value):
        '''Add a value to the Stack'''
        success = True
        #check for full Stack
        if self.isFull():
            success = False
        if success:
            #make a node for the new head that points at the old head
            newNode = Node(value, self.head)
            self.head = newNode
            #only increment currentSize if a value has been added
            self.currentSize += 1
        return success

    def pop(self):
        '''Remove and return value at the front of the Stack'''
        if self.isEmpty():
            success = False
        else:
            #return value at head of Stack
            #make head.next the new head
            head = self.head
            newHead = head.next
            self.head = newHead
            self.currentSize -= 1
            success = head.value
        return success

    def peek(self):
        '''Return value at the front of the Stack'''
        if self.isEmpty():
            success = False
        else:
            success = self.head.value
        return success
