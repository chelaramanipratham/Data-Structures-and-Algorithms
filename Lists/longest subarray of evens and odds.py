#User function Template for python3

class Solution:
    #Function to find the length of longest subarray of even and odd numbers.
    def maxEvenOdd(self,arr,n):
        
        #returns: the maximum length
        
        #code here
        res, curr = 1, 1
        for i in range(1, n):
            if(arr[i] % 2 == 0 and arr[i-1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i-1] % 2 == 0):
                curr += 1
                res = max(curr, res)
            else: curr = 1
            
        return res
