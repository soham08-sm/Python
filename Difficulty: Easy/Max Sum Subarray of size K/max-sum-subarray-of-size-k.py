class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        l=0
        cur_sum=0
        ans=0
        n=len(arr)
        for r in range(n):
            cur_sum+=arr[r]
            while r-l+1>k:
                cur_sum -= arr[l]
                l+=1
            ans = max(ans, cur_sum)
        return ans    