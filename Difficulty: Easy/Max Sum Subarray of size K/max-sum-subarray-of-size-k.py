class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        win_sum = sum(arr[0:k])
        
        
        
        
        maxsum = win_sum
        n = len(arr)
        for i in range (k,n):
            win_sum = win_sum + arr[i] - arr[i-k]
            maxsum = max(maxsum, win_sum)
        return maxsum