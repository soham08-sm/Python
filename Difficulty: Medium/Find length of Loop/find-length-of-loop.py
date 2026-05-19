'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        if not head or not head.next:
            return 0

        slow = fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:          # Cycle detected
                return countLoop(slow)  # Step 2: Count loop length

        return 0                      # No cycle found


def countLoop(node):
    count = 1
    curr = node.next
    while curr != node:               # Traverse until we reach meeting point again
        curr = curr.next
        count += 1
    return count