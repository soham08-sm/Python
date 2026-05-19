'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        # code here
        if not head:
            return head
             
        curr = head 
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        curr = head
        mid = length//2
        for i in range(mid):
            curr = curr.next
            
        return curr.data
        
