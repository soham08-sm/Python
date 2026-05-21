#User function Template for python3
from collections import deque
class Solution:
    def firstNegInt(self, arr, k): 
         # code here 
        queue = deque()
        for i in range(k):
            if arr[i]<0:
                queue.append(i)
                
            result = []
        if queue:
            result.append(arr[queue[0]])
        else:
            result.append(0)
                
        for i in range(k, len(arr)):
            while queue and queue[0]<=i-k:
                queue.popleft()
                    
            if arr[i]<0:
                queue.append(i)
                    
            if queue:
                result.append(arr[queue[0]])
            else:
                result.append(0)
        
        return result