#User function Template for python3

class Solution:
	def reverseDigits(self, n):
		# Code here
        reverse = 0
        
        while n > 0:
            digit = n % 10
            reverse = (10*reverse) + digit
            n = n // 10
            
        return reverse