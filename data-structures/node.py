"""
Node for Linked List Stack and Queue data structures
"""


class Node:
    '''
    Node for a linked list
    '''

    def __init__(self, value, next):
        '''self.value holds value of this node, self.next points to next node'''
        self.value = value
        self.next = next

    def __str__(self):
        return self.value

    def __repr__(self):
        print(f"Node({self.value})")
