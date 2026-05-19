'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        newNode = Node(x)
        if not head:
            return newNode
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        return head
        