'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):
      # code here
        newNode = Node(val)     
        if not head:
            return newNode
        if pos == 1:
            newNode.next = head
            return newNode

        curr = head
        currPos = 1             
        while curr.next and currPos < pos - 1: 
            curr = curr.next
            currPos += 1

        newNode.next = curr.next    
        curr.next = newNode

        return head
      
      

      