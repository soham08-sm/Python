#User function Template for python3

class Solution:
    def sumOfNaturals(self, n):
        # code here 
        if n==0:
            return 0
        return n + self.sumOfNaturals(n-1)