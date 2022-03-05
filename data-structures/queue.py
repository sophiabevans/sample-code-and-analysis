"""
Linked List Queue data structure
"""
from node import Node


class Queue:
	'''First In, First Out (FIFO) linked list'''

	def __init__(self, capacity):
	    '''Create a Queue with capacity > 0 or defaultCapacity'''
	    #check for valid capacity input, else use defaultCapacity
	    if not type(capacity) == int:
	        print("Capacity must be an integer > 0\nDefault capacity used")
	        capacity = defaultCapacity
	    elif capacity <= 0:
	        print("Capacity must be an integer > 0\nDefault capacity used")
	        capacity = defaultCapacity
	    self.tail = None
	    self.head = None
	    self.maxSize = capacity
	    self.currentSize = 0

	def isEmpty(self):
	    '''Return boolean indicating whether Queue is empty'''
	    return self.currentSize == 0

	def isFull(self):
	    '''Return boolean indicating whether Queue is full'''
	    return self.currentSize == self.maxSize

	def enqueue(self, value):
	    '''Add a Node to the Queue'''
	    success = True
	    #check for full Queue or non MealTicket input
	    if self.isFull():
	        success = False
	    #create head Node if Queue is empty
	    elif self.currentSize == 0:
	        self.head = Node(value, self.tail)
	    #create tail Node if Queue only has head node
	    elif self.currentSize == 1:
	        self.tail = Node(value, None)
	        #self.head pointed at None before creating self.tail
	        self.head.next = self.tail
	    else:
	        newNode = Node(value, None)
	        #make self.tail.next point at Node with new MealTicket
	        self.tail.next = newNode
	        #make the newest Node the tail
	        self.tail = newNode
	    if success:
	        #only increment currentSize if a MealTicket has been added
	        self.currentSize += 1
	    return success

	#in assignments 3 and 4 remember to set head.next to None after
	def dequeue(self):
	    '''Remove and return value at the front of the Queue'''
	    if self.isEmpty():
	        success = False
	    else:
	        #return value at head of Queue
	        #make head.next the new head
	        head = self.head
	        self.head = head.next
	        head.next = None
	        self.currentSize -= 1
	        success = head.value
	    return success

	def front(self):
	    '''Return value at the front of the Queue'''
	    if self.isEmpty():
	        success = False
	    else:
	        success = self.head.value
	    return success
